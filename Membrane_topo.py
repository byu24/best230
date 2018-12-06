#This code was made with help from David Quint

from math import sin, cos

pi=3.14159
lc=2			# number of atom rings 
rc=36			# number of atoms per ring
tc=lc*rc

atotl=tc		# total num. of atoms
nbonds=2*tc -rc
atypes=1
btypes=1
chain_ID=1

xbox=110.0		# Sim box size in x dim
ybox=110.0		# Sim box size in y dim
zbox=110.0		# Sim box size in z dim


xboxlo=-xbox		# Set sim box bounds
xboxhi=xbox
yboxlo=-ybox
yboxhi=ybox
zboxlo=-zbox
zboxhi=zbox

R=5.0	 
theta0=2.0*pi/rc
delz=100.0
mass=1.0

posx=0.0
posy=0.0
posz=-zbox+1


filename = 'data.membrane'
foo = open(filename,'w')

print>>foo, "#LAMMPS Data file Monomer-Chain"
print>>foo, " "
print>>foo, atotl,"atoms"
print>>foo, nbonds,"bonds"
print>>foo, atypes,"atom types"
print>>foo, btypes,"bond types"

print>>foo, "%1.1f +%1.1f xlo xhi" % (xboxlo,xboxhi)
print>>foo, "%1.1f +%1.1f ylo yhi" % (yboxlo,yboxhi)
print>>foo, "%1.1f +%1.1f zlo zhi" % (zboxlo,zboxhi)
print>>foo, " "
print>>foo, "Masses"
print>>foo, " "
    
print>>foo, "  %d  %1.1f" % (1, mass) # all the same for now

print>>foo, " "
print>>foo, "Atoms"    #AtomID ChainID ATYPE  xpos  ypos  zpos
print>>foo, " "

k=1
for i in range(lc):
    posz+=i*(delz-1)
    for j in range(rc):
        
        posx = R*cos(j*theta0)
        posy = R*sin(j*theta0)
        print>>foo, " %d %d %d  %1.5f  %1.5f  %1.5f 0 0 0" % (k, atypes, chain_ID, posx, posy, posz)
        k+=1

print>>foo, " "
print>>foo, "Bonds" #BondID  BType     AtomI     AtomJ
print>>foo, " "

k=1
bidex=1
next=0
for i in range(lc):   
    for j in range(rc):	
        print>>foo, "     %d  %d     %d     %d " % (bidex, btypes, j+k, (j+k)%rc+k )
        bidex+=1
    k+=rc
k=0
for i in range(lc-1):   
    for j in range(rc):	
        print>>foo, "     %d  %d     %d     %d " % (bidex, btypes, j+1, (j+1)+rc )
        bidex+=1
foo.close		#Close file
