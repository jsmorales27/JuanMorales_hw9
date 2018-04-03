import matplotlib.pylab as plt
import numpy as np

c=np.loadtxt("times_cpp.txt", dtype=float,delimiter=",")
py=np.loadtxt("times_python.txt", dtype=float,delimiter=",")
print c
print py
plt.scatter(c[:,0],c[:,1],label="C++",color="red")
plt.scatter(py[:,0],py[:,1],label="Python")
plt.legend()
plt.savefig("cpp_vs_python.png")

