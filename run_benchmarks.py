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
        '240',
		'-u',
		'ms',
		'--system-profiling',
		'on']
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

def get_mem_divergence(benchmark_dir):
        
	cd(benchmark_dir)

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

def get_power_stats(benchmark_dir):

	cd(benchmark_dir)

	time.sleep(2)
	time_line = [line for line in grep("Time(%)", "-m", "1", "-A", "2", "test_results.txt").stdout.decode('utf-8').split('\n')]
	time_line = [stat for stat in line[2].split(' ') if stat != '']
	power_line = [stat for stat in grep("Power", "test_results.txt").stdout.decode('utf-8').split('\n')[0].split(' ') if stat != '']
	device = grep("Device", "-m", "1", "test_results.txt").stdout.decode('utf-8').split('\n')[0]

	results = {
		'total_time':float(line[1])/(float(line[0])/100.0),
		'top_kernel_time_pecent':float(line[0]),
		'top_kernel_time_ms':float(line[1]),
		'top_kernel_calls':int(line[2]),
		'top_kernel_avg':float(line[3]),
		'top_kernel_min':float(line[4]),
		'top_kernel_max':float(line[5]),
		'top_kernel_sig':' '.join(line[6:-1]),
		'device':device,
		'power_profiling_count':int(power_line[2]),
		'avg_mW':float(power_line[3]),
		'min_mW':float(power_line[4]),
		'max_mW':float(power_line[5])
	}

	return results

def run_benchmark(benchmakr_dir, args, timeout):

    cd(benchmark_dir)
    try:
        nv = nvprof(*args, _cwd=benchmark_dir, _timeout=timeout, _timeout_signal=SIGINT)
    except TimeoutException as err:
        print(err)

def run_benchmarks(benchmarks, benchmarks_base, timeout):
    default_runs = get_default_run(benchmarks, benchmarks_base)
    results = {}
    for benchmark_dir in default_runs.keys():
        results[benchmark_dir] = []
        for run in default_runs[benchmark_dir]:
            print(benchmarks_base['args_base'] + run)
            try:
				run_benchmark(benchmark_dir, benchmarks_base['args_base'] + [run], timeout)
                #results = get_mem_divergence(benchmark_dir)
				results = get_power_stats(benchmark_dir)
                results[benchmark_dir].append((run, results))
            except ErrorReturnCode as err:
                print(err)
    return results
    
    
results = run_benchmarks(benchmarks, benchmarks_base, 360)


table = []
for benchmark in results:
    for run in results[benchmark]:
        if run:
            #row = [benchmark, run[0], run[1]['gld_min'], run[1]['gld_avg'], run[1]['gld_max'], run[1]['gst_min'], run[1]['gst_avg'], run[1]['gst_max']]
			row = [benchmark, 
					run[0], 
					run[1]['total_time'], 
					run[1]['top_kernel_time_percent'],
					run[1]['top_kernel_time_ms'],
					run[1]['top_kernel_calls'],
					run[1]['top_kernel_avg'],
					run[1]['top_kernel_min'],
					run[1]['top_kernel_max'],
					run[1]['top_kernel_sig'],
					run[1]['device'],
					run[1]['power_profiling_count'],
					run[1]['avg_mW'],
					run[1]['min_mW'],
					run[1]['max_mW']]
				
            table.append(row)
            
cd(benchmarks_base['benchmarks_base_dir'])
#df = pd.DataFrame(table, columns=['benchmark', 'run', 'gld_min', 'gld_avg', 'gld_max', 'gst_min', 'gst_avg', 'gst_max'])
df = pd.DataFrame(table, columns=['benchmark', 'run', 'total_time', 'top_kernel_time_percent', 'top_kernel_time_ms', 'top_kernel_calls', 'top_kernel_avg', 'top_kernel_min', 'top_kernel_max', 'top_kernel_sig', 'device', 'power_profiling_count', 'avg_mW', 'min_mW', 'max_mW'])
df.to_csv('rodinia_metrics.csv')
