include ../../common/make.config


INCLUDE := $(CUDA_DIR)/include

SRC = gaussian.cu
EXE = gaussian

release: $(SRC)
	$(CUDA_CC) $(KERNEL_DIM) $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS) 

clean:
	rm gaussian
