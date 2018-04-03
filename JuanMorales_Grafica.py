import matplotlib.pylab as plt
import numpy as np

c=np.loadtxt("times_cpp.txt", dtype=float,delimiter=",")
py=np.loadtxt("times_python.txt", dtype=float,delimiter=",")

plt.scatter(c[1],c[0],label="C++")
plt.scatter(py[1],py[0],label="Python")
plt.legend()
plt.savefig("cpp_vs_python.png")

