#makefile

include ../../common/make.config

CC := $(CUDA_DIR)/bin/nvcc

INCLUDE := $(CUDA_DIR)/include

all: naive float

naive: ex_particle_CUDA_naive_seq.cu
	$(CC) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS) -lcuda -g -lm -O3 -use_fast_math -arch sm_35 ex_particle_CUDA_naive_seq.cu -o particlefilter_naive 
	
float: ex_particle_CUDA_float_seq.cu
	$(CC) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS) -lcuda -g -lm -O3 -use_fast_math -arch sm_35 ex_particle_CUDA_float_seq.cu -o particlefilter_float

clean:
	rm particlefilter_naive particlefilter_float
