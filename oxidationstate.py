#this script will calculate the oxidation state of given protein based on the paper 'Calculation of the Relative Chemical Stabilities of Proteins as a Function of Temperature and Redox Chemistry in a Hot Spring'
#input: sequence file
#outputfile: oxidation state of every protein sequence

import sys

Pox={} #store the oxidation states of all amino acid based on the paper
Cox={} #stores the toal carbon number for each amino acid based on the paper
Pox['A']=0.00;Pox['C']=0.66;Pox['D']=1.00;Pox['E']=0.40;Pox['F']=-0.44;Pox['G']=1.00;Pox['H']=0.66;Pox['I']=-1.00;Pox['K']=-0.66;Pox['L']=-1.00
Pox['M']=-0.40;Pox['N']=1.00;Pox['P']=-0.40;Pox['Q']=0.40;Pox['R']=0.33;Pox['S']=0.66;Pox['T']=0.00;Pox['V']=-.80;Pox['W']=-0.18;Pox['Y']=-0.22
Cox['A']=3.00;Cox['C']=3.00;Cox['D']=4.00;Cox['E']=5.00;Cox['F']=9.00;Cox['G']=2.00;Cox['H']=6.00;Cox['I']=6.00;Cox['K']=6.00;Cox['L']=6.00
Cox['M']=5.00;Cox['N']=4.00;Cox['P']=5.00;Cox['Q']=5.00;Cox['R']=6.00;Cox['S']=3.00;Cox['T']=4.00;Cox['V']=5.00;Cox['W']=11.00;Cox['Y']=9.00


seq=''
sequence=''
count=0
def findox(name):
	present=0
	tox=0.0
	totalsum=0.0
	totalccount=0.0
	tcount=0
	_aacid={}
	_aacid_1={}
	for key, value in Pox.items():
		for word in name:
			if word==key:
				for tkey,tvalue in Cox.items():
					if word==tkey:
						totalsum=totalsum+tvalue*value
						totalccount+=tvalue
	for tword in name: #calculates the total abundance of specific amino acid residues
		if tword in _aacid.keys():
			_aacid[tword]=_aacid[tword]+1
		else:
			_aacid[tword]=1		
	for tkey,tvalue in _aacid.items():
		_aacid_1[tkey]=float(tvalue)/len(name)
	return (float(totalsum)/totalccount),_aacid_1
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
				#print oxidation,'came'
		#		_store[seq]=float(oxidation)/len(sequence)
				_store[seq]=oxidation
				_specifica[seq]=aminoa
#				outputfile.write(seq+'\t'+str(len(sequence))+'\t'+str(oxidation)+'\t'+str(float(oxidation)/len(sequence))+'\n') #this will spit oxidation state for each sequence so uncomment it if this is what you want.
				sequence=''
			else:
				count=1
			seq=line_strip
		else:
			sequence+=line_strip
	oxidation,aminoa=findox(sequence)
#	_store[seq]=float(oxidation)/len(sequence)
	_store[seq]=oxidation
	#print oxidation,'second'
	_specifica[seq]=aminoa
	return _store,_specifica
#	outputfile.write(seq+'\t'+str(len(sequence))+'\t'+str(oxidation)+'\t'+str(float(oxidation)/len(sequence))+'\n') # this will spit oxidation state of carbon for each sequence so uncomment this if that is what you want.
