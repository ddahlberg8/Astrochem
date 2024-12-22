import os, sys, re
from numpy import *

def cbs23m3l(etz,eqz):
    return 4**3/(4**3-3**3)*eqz - 3**3/(4**3-3**3)*etz 

def cbs45m3l(eqz,e5z):
    return 5**3/(5**3-4**3)*e5z - 4**3/(5**3-4**3)*eqz

def cbs56m3l(e5z,e6z):
    return 6**3/(6**3-5**3)*e6z - 5**3/(6**3-5**3)*e5z

def cbs34m3lt(etz,eqz):
    return 5**3/(5**3-4**3)*eqz - 4**3/(5**3-4**3)*etz

def cbs45m3lt(eqz,e5z):
    return 6**3/(6**3-5**3)*e5z - 5**3/(6**3-5**3)*eqz

def cbs34m4l(etz,eqz):
    return 4**4/(4**4-3**4)*eqz - 3**4/(4**4-3**4)*etz

def cbs45m4half(eqz,e5z):
    return 5.5**4/(5.5**4-4.5**4)*e5z - 4.5**4/(5.5**4-4.5**4)*eqz

def cbs24mix(edz,etz,eqz):
    return (edz*(exp(-2)*exp(-(3**2))-exp(-(2**2))*exp(-3)) - exp(-1)*(etz*exp(-(3**2))-exp(-(2**2))*eqz) + exp(-(1**2))*(etz*exp(-3)-exp(-2)*eqz))/(1*(exp(-2)*exp(-(3**2))-exp(-(2**2))*exp(-3)) - exp(-1)*(1*exp(-(3**2))-exp(-(2**2))*1) + exp(-(1**2))*(1*exp(-3)-exp(-2)*1))

def cbs35mix(etz,eqz,e5z):
    return (etz*(exp(-3)*exp(-(4**2))-exp(-(3**2))*exp(-4)) - exp(-2)*(eqz*exp(-(4**2))-exp(-(3**2))*e5z) + exp(-(2**2))*(eqz*exp(-4)-exp(-3)*e5z))/(1*(exp(-3)*exp(-(4**2))-exp(-(3**2))*exp(-4)) - exp(-2)*(1*exp(-(4**2))-exp(-(3**2))*1) + exp(-(2**2))*(1*exp(-4)-exp(-3)*1))

def fci_dtq(ccsd,ccsdt,ccsdtq):
    return (ccsd) / (1 - ((ccsdt - ccsd) / (ccsd)) / (1 - (ccsdtq - ccsdt) / (ccsdt - ccsd)))

def hf_martin(energy1,energy2,L1,L2):
    return energy2+(energy2-energy1)/(exp(9*(sqrt(L2)-sqrt(L1))-log((L2+1)/(L1+1)))-1)

def fci_dtq_r(ccsd,ccsdt,ccsdtq):
    return ccsd*(1+(ccsdt-ccsd)/ccsd - (ccsdtq-ccsdt)/(ccsdt-ccsd))/(1-(ccsdtq-ccsdt)/(ccsdt-ccsd))

def fci_dtq_q(ccsd,ccsdt,ccsdtq):
    return ccsd+0.5*(ccsdt-ccsd)**2/(ccsdtq-ccsdt)*(1-sqrt(1-4*(ccsdtq-ccsdt)/(ccsdt-ccsd)))

def cbs34m4half(etz,eqz):
    return 4.5**4 / (4.5**4 - 3.5**4) * eqz - 3.5**4 / (4.5**4 - 3.5**4) * etz

def composite_energy(efz,ecvz,ecz):
    return (efz + (ecz - ecvz))

def each_level(dir):
    efz = genfromtxt('%s/energyfz.txt'%dir,skip_header=3)
    ecvz = genfromtxt('%s/energycvz.txt'%dir,skip_header=3)
    ecz = genfromtxt('%s/energycz.txt'%dir,skip_header=3)
    
    efile = open('%s/energyccz.txt'%dir,'w')
    for i in range(2):
        efile.write('\n')
    efile.write("      BOND               ENERHF                 ENERMP2                ENERCCSD               ENERPT\n")
    for j in range(efz.shape[0]):
        if efz[j,0] == ecvz[j,0] and ecz[j,0]:
            efile.write("%16.10f"%ecvz[j,0])
        else:
            print("There is something wrong bond distance, please check!")
        for i in range(1,efz.shape[1]):
            ccz = (efz[j,i] + (ecz[j,i]-ecvz[j,i]))
            efile.write("%23.14f"%ccz)
        efile.write("\n")
    efile.close()

#eqz = genfromtxt('%s/energyqz.txt'%sys.argv[1],skip_header=3)
#e5z = genfromtxt('%s/energy5z.txt'%sys.argv[1],skip_header=3)
#
#efile = open('%s/energyfz.txt'%sys.argv[1],'w')
#for i in range(2):
#    efile.write('\n')
#efile.write("      BOND               ENERHF                 ENERMP2                ENERCCSD               ENERPT\n")
#for j in range(eqz.shape[0]):
#    if eqz[j,0] == e5z[j,0]:
#        efile.write("%16.10f"%eqz[j,0])
#    else:
#        print "There is something wrong bond distance, please check!"
#    for i in range(1,eqz.shape[1]):
#        fz = cbs45m4half(eqz[j,i],e5z[j,i])
#        efile.write("%23.14f"%fz)
#    efile.write("\n")
#efile.close()

def fpa_dat(dir):
    dat = genfromtxt('%s/dat-fpa'%dir)
    eqz = dat[0,:]
    e5z = dat[1,:]
    fz = cbs45m4half(eqz,e5z)
    print(fz)
#    for i in range(len(eqz)):
#        print cb

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: program 1 (1:write cbs-fz at each level;2:print fpa) file directory!")
        sys.exit()
    if sys.argv[1] == '1':
        each_level(sys.argv[2])
    elif sys.argv[1] == '2':
        fpa_dat(sys.argv[2])
    else:
        print("Usage: program 1 (1:write cbs-fz at each level;2:print fpa) file directory!")

