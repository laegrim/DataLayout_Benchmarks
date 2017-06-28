include ../../common/make.config

CC := $(CUDA_DIR)/bin/nvcc
INCLUDE := $(CUDA_DIR)/include

SRC = pathfinder.cu

EXE = pathfinder

release:
	$(CC) $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

enum:
	$(CC) -deviceemu $(SRC) -o $(EXE) -I$(INCLUDE) -L$$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

debug:
	$(CC) -g $(SRC) -o $(EXE) -I$(INCLUDE) -L$$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

debugenum:
	$(CC) -g -deviceemu $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

clean:
	rm -f pathfinder
