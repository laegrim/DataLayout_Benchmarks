include ../../../common/make.config

INCLUDE := $(CUDA_DIR)/include

SRC = srad.cu

EXE = srad

release: $(SRC)
	$(CUDA_CC) $(KERNEL_DIM) $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS) 

enum: $(SRC)
	$(CUDA_CC) $(KERNEL_DIM) -deviceemu $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

debug: $(SRC)
	$(CUDA_CC) $(KERNEL_DIM) -g $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

debugenum: $(SRC)
	$(CUDA_CC) $(KERNEL_DIM) -g -deviceemu $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

clean: $(SRC)
	rm -f $(EXE) $(EXE).linkinfo result.txt
