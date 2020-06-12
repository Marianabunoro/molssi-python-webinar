import numpy 
import os
import argparse
import matplotlib.pyplot as plt



parser = argparse.ArgumentParser(description = "This script parses amber mdout files to extract the total energy.")               
parser.add_argument("mdout_file",  help="The filepath for the mdout file to be analyze")
#parser.add_argument('-make_plot', help= 'generate plot file')
args = parser.parse_args()


file_location = args.mdout_file

mdout = open(file_location, 'r')
data = mdout.readlines()
mdout.close()



#file_name = os.path.basename(file_location)
#file_name = file_name.split('.')[0]
file_name = file_location.split('.')[0]



filehandle = open(str(file_name)+'_E_tot.txt', 'w+')

for lines in data:
    
    if 'A V E R A G E S' in lines:
        break    
    
    if 'Etot' in lines:
        E_tot_aux = lines
        E_tot = E_tot_aux.split()[2]
        filehandle.write(F'{nstep} \t {E_tot} \n' )
    
    if 'NSTEP' in lines:
        nstep_aux = lines
        nstep = nstep_aux.split()[2]
      
  
 
filehandle.close()


#if args.make_plot:
    
#data_plot = numpy.genfromtxt(str(file_name)+'E_tot.txt')
#time = data_plot[:,0]
#E_tot = data_plot[:,1]
#plt.figure()
#plt.plot(time, E_tot)
#plt.xlabel('Time (ps)')
#plt.ylabel('E_total (kcal/mol)')
#plt.savefig(str(filename)+'.png')
    
