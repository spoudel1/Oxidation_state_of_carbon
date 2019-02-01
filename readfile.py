#this script will read fiel from a directory and pass the fiel to oxidatin.py to calculate the average oxidation state of carbon
#input: path to the directory that contains the protein fiel
#outputfile: average oxidation state of each genome

import sys
import oxidationstate
import os
import time

outputfile=open(sys.argv[1],'w')

_store=[]
with open(sys.argv[2],'r') as missedfile:
	for work in missedfile:
		word_strip=work.strip()
		_store.append(word_strip)

def dupcheck(name):
	present=0
	for temp in _store:
		if temp == name:
			present=1
			break
	return present
path="." #folder path that contains genomes/metagenomes
average_ox=0.0
start=time.time()
for root,dirs,files in os.walk(path):
	for tfile in files:
		_newstore={}
		if 'faa' in tfile:
			if dupcheck(tfile)==0:
				genome,spamino=oxidationstate.getfile(path+'/'+tfile)
				average_ox= sum(genome.values())/(len(genome.keys()))
				outputfile.write(tfile+'\t'+str(average_ox))
				count=0
				for key,value in spamino.items():
					for ts,tst in value.items():
						if ts in _newstore.keys():
							_newstore[ts]=_newstore[ts]+tst
						else:
							_newstore[ts]=tst
				for ab, bc in _newstore.items():
						outputfile.write('\t'+ab+'_'+str(float(bc)/(len(genome.keys()))))
			outputfile.write('\n')
#uncomment this if you want to find the protein with high oxidation state. This section will give oxidation state of carbon for top 6 proteins.


#			genome_new=sorted(genome.items(),key=lambda x:x[1])
#			count=1
#			for i in genome_new:
#				if count<6:
#					if count==1:
#						highprotein.write(tfile+'\t'+str(i[0][1:])+'#'+str(i[1]))
#					else:
#						highprotein.write(','+str(i[0][1:]+'#'+str(i[1])))
#				elif count > len(genome_new)-5 and count < len(genome_new)+1:
#					if count ==len(genome_new)-4:
#						highprotein.write('\t'+str(i[0][1:])+'#'+str(i[1]))
#					else:
#						highprotein.write(','+str(i[0][1:])+'#'+str(i[1]))
#				count=count+1
#			highprotein.write('\n')
end=time.time()
print (end-start)
