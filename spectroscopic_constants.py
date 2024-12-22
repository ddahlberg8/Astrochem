import sys
data= sys.argv[1]
energy_file = sys.argv[2]

if ((len(sys.argv) !=3)): 
    print("Error:Only 2 Arguments allowed")
    sys.exit(0)

list1=[]
for i in range(2, 7):
   with open(str(i)+energy_file) as file:        
#iterate this loop for all the energy*z.txt_run.out files files in the directory
#open the Arg 1 file called "data.txt" to append the data
        lines= file.readlines()
        file= open(data,"w")
#For every line in the file read through it but only append it
#if the first _ characters are Norder,The sum, ... ect.
#save this line and slpit it using a space, this creates a list with each word or number as a seperate item in the list
#append the last item in the list which is always the desired value, This is better than specific characters because some values can vary by decimal places
        for line in lines:
            if (line[:7]== " Norder"):
                deriv_order = line[:21]
                deriv = deriv_order.split()	
                list1.append('Norder =' + deriv[-1])
		#list1.append("\n")
	    elif (line[:12]== "     The sum"):
                residual = line[:61]
                residual_c = residual.split()
		list1.append('Residual=' + residual_c[-1])
                #list1.append("\n") 
	    elif (line[:10]== "      Bond"):
                bond = line[:57]
                bond_c = bond.split()
		list1.append('Bond (Anstroms)=' + bond_c[-1])
                #list1.append("\n") 
	    elif (line[:12]== "      Rotati"):
                rotation = line[:57]
                rotation_c = rotation.split()
		list1.append('Rotation (MHz)=' + rotation_c[-1])
                #list1.append("\n") 
	    elif (line[:12]== "      Vibrat"):
                vibration = line[:57]
                vibration_c = vibration.split() 
		list1.append('Vibration (cm-1)=' + vibration_c[-1])
                #list1.append("\n") 
	    elif (line[:12]== "      Centri"):
                centrifugal = line[:57]
                centrifugal_c = centrifugal.split()
		list1.append('Centrifugal (kHz)=' + centrifugal_c[-1])
                #list1.append("\n") 
	    elif (line[:12]== "      Harmon"):
                harmonic = line[:57]
                harmonic_c = harmonic.split()
		list1.append('Harmonic (cm-1)=' + harmonic_c[-1])
                #list1.append("\n") 
	    elif (line[:12]== "      Anharm"):
                anharmonic = line[:57]
                anharmonic_c = anharmonic.split()
		list1.append('Anharmonic (cm-1)=' + anharmonic_c[-1])
                #list1.append("\n") 
#all the data that has been written to is in "list1"
#write out each piece of data in a new line
for j in list1:

    file.write(str(j))
    file.write("\n")

file.close()

