import numpy as np
import numpy.matlib
#testing meshgrid
nx, ny, nz = (4,4,4)
a = np.linspace(-1.5,1.5,nx)
#print(a)
b = np.linspace(-1.5,1.5,ny)
c = np.linspace(-1.5,1.5,nz)
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
Vext = np.sqrt(1/(xv**2 + yv**2 + zv**2))
Vext = -Vext
L = (-2/h**2)*(np.matlib.eye(nx, k=0, dtype=float)) + np.matlib.eye(nx, k=-1, dtype=float) + np.matlib.eye(nx, k=1, dtype=float)
print(L)
