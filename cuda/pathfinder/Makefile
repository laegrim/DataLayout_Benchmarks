include ../../common/make.config

INCLUDE := $(CUDA_DIR)/include

SRC = pathfinder.cu

EXE = pathfinder

release:
	$(CUDA_CC) $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

enum:
	$(CUDA_CC) -deviceemu $(SRC) -o $(EXE) -I$(INCLUDE) -L$$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

debug:
	$(CUDA_CC) -g $(SRC) -o $(EXE) -I$(INCLUDE) -L$$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

debugenum:
	$(CUDA_CC) -g -deviceemu $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) $(CL_NVCC_FLAGS)

clean:
	rm -f pathfinder
