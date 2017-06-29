include ../../../common/make.config

CC = gcc

DEFS += \
		-DGPU_TIMER \
		$(SPACE)

NVCCFLAGS += -I../common \
			 -O3 \
			 -use_fast_math \
			 -arch=sm_35 \
			 -lm \
			 $(SPACE)
NVCCFLAGS += $(CL_NVCC_FLAGS)
CFLAGS += -I../common \
					-I/usr/include/cuda \
		  -O3 \
		  -Wall \
		  $(SPACE)

# Add source files here
EXECUTABLE  := lud_cuda
# Cuda source files (compiled with cudacc)
CUFILES     := lud_kernel.cu
# C/C++ source files (compiled with gcc / c++)
CCFILES     := lud.c lud_cuda.c ../common/common.c

OBJS = ../common/common.o lud.o lud_kernel.o

.PHONY: all clean 
all : $(EXECUTABLE)

.c.o : 
	$(CUDA_CC) $(KERNEL_DIM) $(NVCCFLAGS) $(DEFS) -o $@ -c $<

%.o:	%.cu 
	$(CUDA_CC) $(KERNEL_DIM) $(NVCCFLAGS) $(DEFS) -o $@ -c $<


$(EXECUTABLE) : $(OBJS)
	$(CUDA_CC) $(NVCCFLAGS) -o $@  $?

clean:
	rm -f $(EXECUTABLE) $(OBJS) *.linkinfo
