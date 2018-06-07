import csv
import os,glob
path='C:\TempDir\LandingZone\\'
os.chdir(path)
filename= glob.glob('ericsson_utran_cm_locell*.asv');
file=path+filename[0]
outputfilename='ElectricalAntennaTilt.csv'
outputpath='C:\TempDir\ExtData\\'
outputfile=outputpath+outputfilename;

with open(file,'r') as csvfile:
    readCSV=csv.reader(csvfile,delimiter='|')
    with open(outputfile,'w') as outputcsvfile:
        writeCSV=csv.writer(outputcsvfile,delimiter=',')
        for row in readCSV:
            writeCSV.writerow(row);
