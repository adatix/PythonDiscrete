import csv

with open('C:\TempDir\ericsson_utran_cm_locell_05062018.asv','r') as csvfile:
    readCSV=csv.reader(csvfile,delimiter='|')
# for row in readCSV:
# print(row[1],row[4],row[29])
    with open('C:\TempDir\ElectricalAntennaTilt.csv','w') as outputcsvfile:
        writeCSV=csv.writer(outputcsvfile,delimiter=',')
        for row in readCSV:
            writeCSV.writerow(row);