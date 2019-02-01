#this script will calculate the oxidation state of given protein based on the paper 'Calculation of the Relative Chemical Stabilities of Proteins as a Function of Temperature and Redox Chemistry in a Hot Spring'
#input: sequence file
#outputfile: oxidation state of every protein sequence

import sys

#inputfile=open(sys.argv[1]).readlines()
#outputfile=open(sys.argv[2],'w')
Pox={} #store the oxidation states of all amino acid based on the paper
Pox['A']=0.00;Pox['C']=0.66;Pox['D']=1.00;Pox['E']=0.40;Pox['F']=-0.44;Pox['G']=1.00;Pox['H']=0.66;Pox['I']=-1.00;Pox['K']=-0.66;Pox['L']=-1.00
Pox['M']=-0.40;Pox['N']=1.00;Pox['P']=-0.40;Pox['Q']=0.40;Pox['R']=0.33;Pox['S']=0.66;Pox['T']=0.00;Pox['V']=-.80;Pox['W']=-0.18;Pox['Y']=-0.22

seq=''
sequence=''
count=0
def findox(name):
	present=0
	tox=0.0
	totalsum=0.0	
	tcount=0
	_aacid={}
	_aacid_1={}
	for key, value in Pox.items():
		for word in name:
			if word==key:
				totalsum+=value
	for tword in name: #calculates the total abundance of specific amino acid residues
		if tword in _aacid.keys():
			_aacid[tword]=_aacid[tword]+1
		else:
			_aacid[tword]=1		
	for tkey,tvalue in _aacid.items():
		_aacid_1[tkey]=float(tvalue)/len(name)
	return totalsum,_aacid_1
def getfile(file1):
	count=0
	sequence=''
	seq=''
	_store={}
	_specifica={}
	inputfile=open(file1).readlines()
	for line in inputfile:
		line_strip=line.strip()
		if line_strip.startswith('>'):
			if count>0:
				oxidation,aminoa=findox(sequence)
				_store[seq]=float(oxidation)/len(sequence)
				_specifica[seq]=aminoa
#				outputfile.write(seq+'\t'+str(len(sequence))+'\t'+str(oxidation)+'\t'+str(float(oxidation)/len(sequence))+'\n')
				sequence=''
			else:
				count=1
			seq=line_strip
		else:
			sequence+=line_strip
	oxidation,aminoa=findox(sequence)
	_store[seq]=float(oxidation)/len(sequence)
	_specifica[seq]=aminoa
	return _store,_specifica
#	outputfile.write(seq+'\t'+str(len(sequence))+'\t'+str(oxidation)+'\t'+str(float(oxidation)/len(sequence))+'\n')
