import time
import numpy as np

def fibonacci(N):
	if N<=1:
		return N
	else:
		return fibonacci(N-1)+fibonacci(N-2)

def get_time(N):
	t0 = time.time()
	fibonacci(N)
	t1 = time.time()-t0
	return t1

lista=np.linspace(0,35,35)
for j in range (0,36):
	print j,",",get_time(j)
