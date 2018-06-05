import csv

with open('C:\TempDir\ericsson_utran_cm_locell_05062018.asv','r') as csvfile:
    readCSV=csv.DictReader(csvfile)
# for row in readCSV:
# print(row[1],row[4],row[29])
    with open('C:\TempDir\ElectricalAntennaTilt.csv','w') as outputcsvfile:
        fieldnames=['ELEMENT_NAME','DATE','electricalAntennaTilt']
        writeCSV=csv.DictWriter(outputcsvfile,fieldnames=fieldnames,delimiter=',')
        writeCSV.writeheader()
        for row in readCSV:
            del row[0]
            writeCSV.writerow(row);