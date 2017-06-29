include ../../common/make.config

CC = g++

CUDA_INCLUDEPATH=/usr/local/cuda/include

NVCC_OPTS=-O3 -arch=sm_35 -Xcompiler -m64 -g -G
NVCC_OPTS += $(CL_NVCC_FLAGS)

GCC_OPTS=-O3 -Wall -Wextra -m64

OBJ = main_test_cu.o stats_logger.o vlc_kernel_sm64huff.o scan.o pack_kernels.o cpuencode.o
SRC = main_test_cu.cu
EXE = pavle

ifdef TESTING 
override TESTING = -DTESTING
endif

ifdef CACHECWLUT
override TESTING = -DCACHECWLUT
endif

pavle: $(OBJ) 
	$(CUDA_CC) $(TESTING) $(CACHECWLUT) $(NVCC_OPTS) $(OBJ) -o $(EXE) 

vlc_kernel_sm64huff.o: vlc_kernel_sm64huff.cu 
	$(CUDA_CC) $(TESTING) -c vlc_kernel_sm64huff.cu $(NVCC_OPTS)

scan.o: scan.cu 
	$(CUDA_CC) -c scan.cu $(NVCC_OPTS)

#cpuencode.o: cpuencode.cu
#	$(CUDA_CC) -c $(NVCC_OPTS) cpuencode.cu

pack_kernels.o: pack_kernels.cu 
	$(CUDA_CC) -c pack_kernels.cu $(NVCC_OPTS)

main_test_cu.o: main_test_cu.cu cutil.h
	$(CUDA_CC) $(TESTING) -c main_test_cu.cu $(NVCC_OPTS) -I $(CUDA_INCLUDEPATH) 

.o:.cpp
	$(CC) ++ $(GCC_OPTS) -c $@ -o $<

clean:
	rm -f *.o $(EXE) 
