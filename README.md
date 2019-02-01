These scripts will calulate the average oxidation state of carbon for a given genome or metagenome. Here, the average oxidation state of carbon for each amino-acid is taken from the paper: 
'Dick, Jeffrey M., and Everett L. Shock. "Calculation of the relative chemical stabilities of proteins as a function of temperature and redox chemistry in a hot spring." PLoS One 6.8 (2011): e22782.'

Two scripts were generated to calculate the oxidation state:
1) readfile.py - this script will accept multiple protein sequence files and individually pass it to oxidatonstate.py script. The oxidation state of carbon calculated will be normalized based on the number of protein sequences present in the file.
2) oxidationstate.py - this script will read each protein sequnece and calculate the oxidation state of carbon for the each sequence. 


Please cite this paper if you decide to use these scripts:
1) Poudel, Saroj, et al. "Electron transfer to nitrogenase in different genomic and metabolic backgrounds." Journal of bacteriology (2018): JB-00757.

