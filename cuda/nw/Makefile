include ../../common/make.config

CC := $(CUDA_DIR)/bin/nvcc

INCLUDE := $(CUDA_DIR)/include

SRC = needle.cu

EXE = needle

release: $(SRC)
	$(CC) ${KERNEL_DIM} $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

enum: $(SRC)
	$(CC) ${KERNEL_DIM} -deviceemu $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

debug: $(SRC)
	$(CC) ${KERNEL_DIM} -g $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

debugenum: $(SRC)
	$(CC) ${KERNEL_DIM} -g -deviceemu $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

clean: $(SRC)
	rm -f $(EXE) $(EXE).linkinfo result.txt
