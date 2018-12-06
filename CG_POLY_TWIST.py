#This code was made with help from David Quint

# python script to generate chain 
from math import sin, cos

pi=3.14159
mass=[]			# atom masses
n=100   			# num. of atoms in chain
ns=n			# num. atoms in backbone

atypes=2		# types of atoms
btypes=2		# types of bonds
antypes=2		# types of angles

atotl=n+ns		# total num. of atoms
nbonds=atotl-1		# num. of bonds
nan=antypes*ns-2	# Number of angles	
		
chain_ID=1 		# ploymer chain ID
ang_ID=1		# angle ID

mass.append(10.0)		# Mass for atoms (defualt 1.0 for all)
mass.append(100.0)
q1=0.0
q2=0.0


xbox=110.0		# Sim box size in x dim
ybox=110.0		# Sim box size in y dim
zbox=110.0		# Sim box size in z dim


xboxlo=-xbox		# Set sim box bounds
xboxhi=xbox
yboxlo=-ybox
yboxhi=ybox
zboxlo=-zbox
zboxhi=zbox


posx=0.0		# Initailize atom positions
posy=0.0
posz=-zbox
delz=1.0		# z spacing
theta0=2.0*pi/n		# pitch angle
L=0.5			# length of backbone bonds

for i in range (1):#(mol_ring+1):
    filename = 'data.chain%d'%(i,)
    foo = open(filename,'w')
    
    print>>foo, "#LAMMPS Data file Monomer-Chain"
    print>>foo, " "
    print>>foo, atotl,"atoms"
    print>>foo, nbonds,"bonds"
    print>>foo, nan,"angles"
    print>>foo, atypes,"atom types"
    print>>foo, btypes,"bond types"
    print>>foo, antypes,"angle types"

    print>>foo, "%1.1f +%1.1f xlo xhi" % (xboxlo,xboxhi)
    print>>foo, "%1.1f +%1.1f ylo yhi" % (yboxlo,yboxhi)
    print>>foo, "%1.1f +%1.1f zlo zhi" % (zboxlo,zboxhi)
    print>>foo, " "
    print>>foo, "Masses"
    print>>foo, " "
    
    for j in range(atypes):
        print>>foo, "  %d  %1.1f" % (j+1, mass[j]) # all the same for now

    print>>foo, " "
    print>>foo, "Atoms"    #AtomID ChainID ATYPE  xpos  ypos  zpos
    print>>foo, " "
        
    j=1
    k=1
    s=0
    for j in range(atotl):
               
        if (j+1)%2==0:
           s=1
           theta=theta0+(j)*theta0	 
           posx=L*cos(theta)	#X position on the CHAIN
           posy=L*sin(theta)	#Y position on the CHAIN 
        else:
           s=0

           posx=0.0
           posy=0.0
           posz+=delz		#Z position on the CHAIN

   	print>>foo, " %d %d %d  %1.5f  %1.5f  %1.5f 0 0 0" % (k, atypes-s, chain_ID+s, posx, posy, posz)
	k+=1
	
    
    print>>foo, " "
    print>>foo, "Angles"    #AngleID AngleType atom#1 atom#2 atom#3
    print>>foo, " "

    k=1
    anidex=1
 
    for j in range(nan):

	if anidex%2==0:
           print>>foo, "     %d %d  %d %d %d" % (anidex, antypes-1, k, k+2, k+3)
           k+=2        

        else:
           print>>foo, "     %d %d  %d %d %d" % (anidex, antypes, k+1, k, k+3) 
        anidex+=1

    print>>foo, " "
    print>>foo, "Bonds" #BondID  BType     AtomI     AtomJ
    print>>foo, " "
    
    k=1
    bidex=1	# we need the bond index to start at 1
    s=0
    for j in range(n):
	print>>foo, "     %d  %d     %d     %d " % (bidex, btypes,2*j+1, 2*k)
	if k<n:
	   print>>foo, "     %d  %d     %d     %d " % (bidex+1, btypes-1,2*j+1, 2*k+1)
	k+=1
	bidex+=2
	if j%2==0:
           s=1
        else:
           s=0 
	
   	
    foo.close		#Close file

