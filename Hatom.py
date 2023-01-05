import numpy as np
import numpy.matlib
import sys
import numpy

'''
Setting display threshold to maximum for numpy arrays.
Helps in easy debugging of code.
'''
numpy.set_printoptions(threshold=sys.maxsize)

#testing meshgrid
'''
Defining number of grid points required along each axis.
Confining the interval in each dimension.
'''
nx, ny, nz = (18,18,18)
a = np.linspace(-30,30,nx)
#print(a)
b = np.linspace(-30,30,ny)
c = np.linspace(-30,30,nz)
#print(x,y)
'''
Generating grid points in 3D space where potential will be evaluated.
'''
xv, yv, zv = np.meshgrid(a,b,c, indexing='xy')
# print(xv, end="--------")

#testing the grid points are generated correctly.
# input()
# for l in range(nx):
#     for m in range(ny):
#         for n in range(nz):
#             print(xv)
        

#grid spacing
h = a[2]-a[1]
'''
Writing external potential for each point of the grid from origin.
Considering proton at the center of the mesh.
Using hartree units for energies and potential.
'''
Vext = -1*(np.sqrt(1/(xv**2 + yv**2 + zv**2)))

'''
Genrating Langrangen matrix consisting of 
1 on left and right diagonal
-2 on diagonal.Also called hessian.

This matrix comes from system of linear equations of the form AX=B, taking into accont the two neighbour when 1D.
Simply put, it is 1D laplacian.
'''
L = (-2/h**2)*(np.matlib.eye(nx, k=0, dtype=float)) + (1/h**2)*(np.matlib.eye(nx, k=-1, dtype=float)) + (1/h**2)*(np.matlib.eye(nx, k=1, dtype=float))
I = np.eye(nx)

'''
To expand 1D descrete laplacian in 3D, we use kroneker product of matrices.
'''
L3 = np.kron(np.kron(L,I),I) + np.kron(np.kron(I,L),I) + np.kron(np.kron(I,I),L)
Vd = Vext.flatten()
V = np.diag(Vd)
#print(len(V))
#print(len(V[0]))

'''
Solving for eigen values and eigen vector gives us energy of each grid point.
From them, the result is the minimum eigen value i.e. the ground state of system.
'''
eigen_val, eigen_vec = np.linalg.eig(-0.5*L3 + V)
print(min(eigen_val)*27.215)
