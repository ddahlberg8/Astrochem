import sys, os
from numpy import *

efile = sys.argv[1]
iatom = sys.argv[2]
order = ['6', '5', '4', '3', '2',]
basis = 'energy'+efile[6:-4]+'.txt'
dat=genfromtxt(efile,skip_header=3,dtype='str')
## col0: bond
## col1: rhf
## col2: mp2
## col3: ccsd
## col4: ccsd_t
eall  = ['scf', 'mp2','ccsd','ccsd_t']
bonds = dat[:,0].astype(float)
atoms = iatom.split(',')

for j in range(len(order)):
    for i in range(4):
        energy = dat[:,i+1]
        name = eall[i]
        deriv = order[j]
        frun = open('%s/%s_run'%(name,deriv + '-' + basis),'w')

        frun.write('1\n')
        frun.write('title\n')
        frun.write('%s,%s,0,0\n'%(len(energy),order[j]))
        frun.write('%10.8f\n'%bonds[int(len(energy)/2)])
        for k in range(len(bonds)):
            frun.write('%10.8f,'%bonds[k])
            frun.write('%12s'%'-0.')
            frun.write('%s\n'%energy[k].split('.')[-1][:])
#           frun.write('%s\n'%energy[j].split('.')[-1][:-3])
#        atoms = ['56','31']
        for atom in atoms:
            frun.write('%s\n'%atom)
        frun.write('end of input')
        
    
        frun.close()
