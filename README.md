allderiv_write_run_fit1d.py
    Arg1 - energynz.txt_run.out (where n = t,q,5,f…)
    Arg 2 - atomic mass of the most abundant isotope of the atom separated by a comma (56,31) for FeP and (58,31) for NiP

This is a script I wrote to help speed up the process of data collection. After running a successful quantum calculation on a molecule we needed to use energy points in the output file to calculate spectroscopic constants. The script to calculate the constants was already written (fit1d script), but this script would take the data points from the output file and make an input file for fit1d to calculate the spectroscopic constants. This script also creates input file for each derivative of the taylor expansion of the fit1d (2-6) instead of running the script 5 separate times.

spectroscopic_constants.py
    Arg1 – data.txt
    Arg2 – -energynz.txt_run.out (where n = t,q,5,f…)

After the fit1d script produced output files containing the data we needed, this script would take the data from all 5 output files and compile into 1 simple text file that I would further organize in excel. “-energynz.txt_run.out” allows the script to cycle through all the output files at the different orders (2-6)

composite.py
Arg1 - 1

The nature of the quantum chemistry work we were doing was that we could use different theoretical frameworks and then manipulate the answer from several different theories to approximate the best answer. Some of this script existed already, but I did some troubleshooting and made some additions in order to expand the scope of the script and increase the data manipulations we were able to do.


pdb-script.py
Arg1 – the input pdb file
Arg2 – the output file that contains the organized pdb information

The goal of the  protein software development project was to trim the protein databank files (pdb file) in such a way to include the important parts of the enzyme that were chemically involved in the reaction, but not include atoms that were not involved which would speed up the computation time. This script was a part of that process and removed unwanted lines from the pdb file and add the necessary information to run the quantum mechanics computation. 
