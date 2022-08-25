import numpy as np
import numpy.matlib
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
#testing meshgrid
nx, ny, nz = (18,18,18)
a = np.linspace(-30,30,nx)
#print(a)
b = np.linspace(-30,30,ny)
c = np.linspace(-30,30,nz)
#print(x,y)
xv, yv, zv = np.meshgrid(a,b,c, indexing='xy')
# print(xv, end="--------")

#test
# input()
# for l in range(nx):
#     for m in range(ny):
#         for n in range(nz):
#             print(xv)
        

#grid spacing
h = a[2]-a[1]
Vext = -1*(np.sqrt(1/(xv**2 + yv**2 + zv**2)))

L = (-2/h**2)*(np.matlib.eye(nx, k=0, dtype=float)) + (1/h**2)*(np.matlib.eye(nx, k=-1, dtype=float)) + (1/h**2)*(np.matlib.eye(nx, k=1, dtype=float))
I = np.eye(nx)
L3 = np.kron(np.kron(L,I),I) + np.kron(np.kron(I,L),I) + np.kron(np.kron(I,I),L)
Vd = Vext.flatten()
V = np.diag(Vd)
print(len(V))
print(len(V[0]))
eigen_val, eigen_vec = np.linalg.eig(-0.5*L3 + V)
print(min(eigen_val)*27.215)
