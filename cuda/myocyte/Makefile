include ../../common/make.config
# Example
# target: dependencies
	# command 1
	# command 2
          # .
          # .
          # .
	# command n

# link objects(binaries) together
myocyte.out:		main.o
	$(CUDA_CC)	main.o \
				-I/usr/local/cuda/include \
				-L/usr/local/cuda/lib \
				-lm -lcuda -lcudart \
                                -o myocyte.out

# compile main function file into object (binary)
main.o:	define.c \
				main.cu \
				work.cu \
				solver.cu \
				embedded_fehlberg_7_8.cu \
				master.cu \
				kernel.cu \
				kernel_ecc.cu \
				kernel_cam.cu \
				kernel_fin.cu \
				work_2.cu \
				solver_2.cu \
				embedded_fehlberg_7_8_2.cu \
				kernel_2.cu \
				kernel_ecc_2.cu \
				kernel_cam_2.cu \
				kernel_fin_2.cu \
				file.c \
				timer.c
	$(CUDA_CC)	main.cu \
				-c -O3 -g $(CL_NVCC_FLAGS)

# delete all object files
clean:
	rm *.o *.out output.txt
