import numpy as np
#testing meshgrid
nx, ny, nz = (2,2,2)
a = np.linspace(0,2,nx)
#print(a)
b = np.linspace(2,4,ny)
c = np.linspace(4,6,nz)
#print(x,y)
xv, yv, zv = np.meshgrid(a,b,c, indexing='xy')
# print(xv, end="--------")


# input()
# for l in range(nx):
#     for m in range(ny):
#         for n in range(nz):
#             print(xv)
        
i=0
print(xv[i,i,i])
