#README
#BEST 230 Molecular Dynamics Project by Brenda Yu
#Simulates a DNA strand in a cylindrical tube

#Install LAMMPS from https://lammps.sandia.gov/
#Follow directions to install
#rename lammps file to lammps
#install different LAMMPS packages that you can find on website too
make ps
make yes-molecule
make yes-python
make install

#The following assumes Python and LAMMPS are installed in Bash

#Create environment
conda create -n best230 python=3.6 anaconda #replace best230 with whatever environment name you want
source activate best230

#Activate LAMMPS serial before you can run your code
cd /lammps/src
pwd
LAMMPS_DIR=$PWD
export PATH=$LAMMPS_DIR:$PATH
make ps #if the package you need is not installed
make serial

#Upload directory files
cd .. #(to desired directory with files)

#Run python files first
#Run LAMMPS files (in.* files)
lmp_serial -in in.helix.chain #repeat the same for the other in.* files

#produces *.lammpstrj files that have xyz coordinates

#export *.lammpstrj files into Visual Molecular Dynamics (VMD)
#Load new molecule into VMD
#Play video to view simulation

