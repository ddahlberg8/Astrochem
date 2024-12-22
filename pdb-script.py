import sys

input_file= sys.argv[1]
output_file= sys.argv[2]

if ((len(sys.argv) !=3)): 
    print("Error: Only 2 arguments are permitted")
    sys.exit(0)

else:
    print("correct number of arguments")
#open pdb file
with open(input_file) as file:
    lines= file.readlines()
#open the file to print in
file= open(output_file,"w")
#blank list to store the lines of interest
xyz_coordinates = []
for line in lines:
    if (line[:3]== "ATO" or line[:6]=="HETATM") and line[11:16] =="  CA ":
        xyz_coordinates.append(line[0:80]) 
        complete_line = line[:80]+"  -1 \n"
        file.write(complete_line)
        #file.write("-1") to freeze the atom
    elif  (line[:3]== "ATO" or line[:6]=="HETATM") and line[11:16] !="  CA ":
        xyz_coordinates.append(line[0:80])
        complete_line2 = line[:80]+"  0 \n"
        file.write(complete_line2)
        #file.write("0")
file.close()
