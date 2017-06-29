include ../../common/make.config

CC := $(CUDA_CC)

INCLUDE := $(CUDA_DIR)/include

SRC = bfs.cu

EXE = bfs

release: $(SRC)
	$(CC) $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS) 

enum: $(SRC)
	$(CC) -deviceemu $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

debug: $(SRC)
	$(CC) -g $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

debugenum: $(SRC)
	$(CC) -g -deviceemu $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

clean: $(SRC)
	rm -f $(EXE) $(EXE).linkinfo result.txt
