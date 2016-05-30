import pencil as pc 
import os
import numpy as N
from math import *
varfrom=raw_input('from :')
varto=raw_input('to :')
dim=pc.read_dim()
grid=pc.read_grid(quiet=True)
uu1=pc.read_slices(field='uu1',extension='xy')
uu2=pc.read_slices(field='uu2',extension='xy')
uu3=pc.read_slices(field='uu3',extension='xy')
fl=open('avg5-9.dat','w')
fl.write('VARIABLES="x","y","Ux","Uy","Uz","U2","V2","W2","UV","UW","VW"\n')
print >>fl, 'ZONE I=%d,J=%d,F=POINT\n'  %(dim.ny,dim.nx)
nslice=0
avgu=N.zeros([3,dim.my,dim.mx],dtype=N.double)
avgu2=N.zeros([6,dim.my,dim.mx],dtype=N.double)
for ts,sliceu,slicev,slicew in zip(uu1[1],uu1[0],uu2[0],uu3[0]):
##for ts,sliceu,slicev in zip(uu1[1],uu1[0],uu2[0]):
    if ts>float(varfrom) and ts<float(varto):
        nslice=nslice+1
        print('begin write ......var.dat'+str(ts))
        for i in range(dim.l1,dim.l2+1):
            for j in range(dim.m1,dim.m2+1):
                avgu[0,j,i]=avgu[0,j,i]+sliceu[j-3,i-3]
                avgu[1,j,i]=avgu[1,j,i]+slicev[j-3,i-3]
                avgu[2,j,i]=avgu[2,j,i]+slicew[j-3,i-3]
                avgu2[0,j,i]=avgu2[0,j,i]+sliceu[j-3,i-3]*sliceu[j-3,i-3]
                avgu2[1,j,i]=avgu2[1,j,i]+slicev[j-3,i-3]*slicev[j-3,i-3]
                avgu2[2,j,i]=avgu2[2,j,i]+slicew[j-3,i-3]*slicew[j-3,i-3]
                avgu2[3,j,i]=avgu2[3,j,i]+sliceu[j-3,i-3]*slicev[j-3,i-3]
                avgu2[4,j,i]=avgu2[4,j,i]+sliceu[j-3,i-3]*slicew[j-3,i-3]
                avgu2[5,j,i]=avgu2[5,j,i]+slicev[j-3,i-3]*slicew[j-3,i-3]
avgu=avgu/nslice
avgu2=avgu2/nslice
avgu2[0,:,:]=avgu2[0,:,:]-avgu[0,:,:]*avgu[0,:,:]
avgu2[1,:,:]=avgu2[1,:,:]-avgu[1,:,:]*avgu[1,:,:]
avgu2[2,:,:]=avgu2[2,:,:]-avgu[2,:,:]*avgu[2,:,:]
avgu2[3,:,:]=avgu2[3,:,:]-avgu[0,:,:]*avgu[1,:,:]
avgu2[4,:,:]=avgu2[4,:,:]-avgu[0,:,:]*avgu[2,:,:]
avgu2[5,:,:]=avgu2[5,:,:]-avgu[1,:,:]*avgu[2,:,:]
for i in range(dim.l1,dim.l2+1):
    for j in range(dim.m1,dim.m2+1):
        fl.write(str(grid.x[i])+' ' + str(grid.y[j])+' '+str(avgu[0,j,i])+' '+str(avgu[1,j,i])+' '+str(avgu[2,j,i])+' '+str(avgu2[0,j,i])+' '+str(avgu2[1,j,i])+' '+str(avgu2[2,j,i])+' '+str(avgu2[3,j,i])+' '+str(avgu2[4,j,i])+' '+str(avgu2[5,j,i])+'\n')
fl.close()                    
    #pos[ts]=xlocation(0,slice[dim.ny/2,:],dim,grid)
    #psd[ts]=slice[dim.ny/2,dim.nx/2]
#for p in range(int(varfrom),int(varto)):
    #var=pc.read_var(quiet=True,ivar=p)
    #uy=var.uy[(dim.n1+dim.n2)/2,:,:]
    #uz=var.uz[(dim.n1+dim.n2)/2,:,:]
    #ux=var.ux[(dim.n1+dim.n2)/2,:,:]
    #lnrho=var.lnrho[(dim.n1+dim.n2)/2,:,:]
    #fl=open('res/bin'+str(p)+'.dat','w')
    #fl.write('VARIABLES="x","y","Ux","Uy","lnrho"\n')
    #print >>fl, 'ZONE I=%d,J=%d,F=POINT\n'  %(dim.ny,dim.nx)
    #for i in range(dim.l1,dim.l2+1):
        #for j in range(dim.m1,dim.m2+1):
                #fl.write(str(var.x[i])+' ' + str(var.y[j])+' '+str(ux[j,i])+' '+str(uy[j,i])+' '+str(lnrho[j,i])+'\n')
    #fl.close()
#os.system('preplot res/bin.dat res/avg.plt' )
#os.remove('res/bin.dat')                   

=======
dfadfthis is a wrong file
