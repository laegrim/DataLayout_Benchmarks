include ~/rodinia_3.1/common/make.config

INCLUDE := $(CUDA_DIR)/include

SRC = 3D.cu

EXE = 3D 

OUTPUT = *.out

FLAGS = -g -G #-arch sm_35 --ptxas-options=-v
FLAGS += $(CL_NVCC_FLAGS)

release: $(SRC)
	$(CUDA_CC) $(KERNEL_DIM) $(FLAGS) $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) 

enum: $(SRC)
	$(CUDA_CC) $(KERNEL_DIM) $(FLAGS) -deviceemu $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) 

debug: $(SRC)
	$(CUDA_CC) $(KERNEL_DIM) $(FLAGS) -g $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) 

debugenum: $(SRC)
	$(CUDA_CC) $(KERNEL_DIM) $(FLAGS) -g -deviceemu $(SRC) -o $(EXE) -I$(INCLUDE) -L$(CUDA_LIB_DIR) 

clean: $(SRC)
	rm -f $(EXE) $(EXE).linkinfo $(OUTPUT) 
