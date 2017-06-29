import sh
from signal import SIGINT, SIGTERM
from sh import nvprof, cd, cat, grep
from sh import ErrorReturnCode, ErrorReturnCode_1, TimeoutException
import pandas as pd
import time


benchmarks_base = {}
benchmarks_base['benchmarks_base_dir'] = '/home/st1289/rodinia_3.1/cuda/'
benchmarks_base['data_base_dir'] = '/home/st1289/rodinia_3.1/data/'
benchmarks_base['args_base'] =  ['--metrics',
       'gld_transactions_per_request,gst_transactions_per_request',
       '--log-file',
       'results.txt',
        '--timeout',
        '240']
benchmarks = ['backprop',
              'bfs',
              'b+tree',
              'cfd',
              'dwt2d',
              'gaussian',
              'heartwall',
              'hotspot',
              'hotspot3D',
              'huffman',
              'hybridsort',
              'kmeans',
              'lavaMD',
              'leukocyte/CUDA',
	      'leukocyte',
              'lud',
              'myocyte',
              'nn',
              'nw',
              'particlefilter',
              'pathfinder',
              'srad/srad_v1',
	      'srad/srad_v2',
              'streamcluster',
              'mummergpu',
             ]

def get_default_run(benchmarks, benchmarks_base):
    default_runs = {}
    for benchmark in benchmarks:
        benchmark_dir = benchmarks_base['benchmarks_base_dir'] + benchmark
        try:
            cd(benchmark_dir)
            defaults = [line for line in cat('run').stdout.decode('utf-8').split('\n') if './' in line]
            defaults = [line for line in defaults if '#' not in line]
            defaults = [line.split(' ') for line in defaults]
            default_runs[benchmark_dir] = defaults
        except ErrorReturnCode as err:
            print(err)
            
    return default_runs

def get_mem_divergence(benchmark_dir, args, timeout):
        
    cd(benchmark_dir)
    try:
        nv = nvprof(*args, _cwd=benchmark_dir, _timeout=timeout, _timeout_signal=SIGINT)
    except TimeoutException as err:
        print(err)
        
    time.sleep(2)
    mem_lines = grep('transactions_per_request', 'results.txt')
    mem_lines = mem_lines.stdout.decode('utf-8')
    mem_lines = [string for string in mem_lines.split(' ') if string]
    results = {
    'gld_min' : float(mem_lines[7]),
    'gld_max' : float(mem_lines[8]),
    'gld_avg' : float(mem_lines[9].strip('\n')),
    'gst_min' : float(mem_lines[-1]),
    'gst_max' : float(mem_lines[-2]),
    'gst_avg' : float(mem_lines[-3].strip('\n')),
    }
    
    return results

def run_benchmarks(benchmarks, benchmarks_base, timeout):
    default_runs = get_default_run(benchmarks, benchmarks_base)
    results = {}
    for benchmark_dir in default_runs.keys():
        results[benchmark_dir] = []
        for run in default_runs[benchmark_dir]:
            print(benchmarks_base['args_base'] + run)
            try:
                result = get_mem_divergence(benchmark_dir, benchmarks_base['args_base'] + [run], timeout)
            	results[benchmark_dir].append((run, result))
            except ErrorReturnCode as err:
                print(err)
    return results
    
    
results = run_benchmarks(benchmarks, benchmarks_base, 360)


table = []
for benchmark in results:
    for run in results[benchmark]:
        if run:
            row = [benchmark, run[0], run[1]['gld_min'], run [1]['gld_avg'], run[1]['gld_max'], run[1]['gst_min'], run[1]['gst_avg'], run[1]['gst_max']]
            table.append(row)
            
cd(benchmarks_base['benchmarks_base_dir'])
df = pd.DataFrame(table, columns=['benchmark', 'run', 'gld_min', 'gld_avg', 'gld_max', 'gst_min', 'gst_avg', 'gst_max'])
df.to_csv('rodinia_metrics.csv')
