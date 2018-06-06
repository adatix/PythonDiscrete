import csv
import os,glob
path='C:\TempDir\\'
os.chdir(path)
filename= glob.glob('ericsson_utran_cm_locell*.asv');
file=path+filename[0]
with open(file,'r') as csvfile:
    readCSV=csv.reader(csvfile,delimiter='|')
    with open('C:\TempDir\ElectricalAntennaTilt.csv','w') as outputcsvfile:
        writeCSV=csv.writer(outputcsvfile,delimiter=',')
        for row in readCSV:
            writeCSV.writerow(row);
