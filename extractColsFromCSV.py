import codecs
import re
import csv

inputCSV = "asd.csv"

output = {}
output['A'] = list()
output['B'] = list()
output['C'] = list()
with codecs.open( inputCSV, "r", "utf-8" ) as f:
    reader = csv.reader(f, delimiter=',')
    for cells in reader:
    	output['A'].append(cells[7])
    	output['B'].append(cells[14])
    	output['C'].append(cells[15])


with codecs.open( "op-" + fname, "w", "utf-8" ) as csvfile:
    fieldnames = ['A', 'B', 'C']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    i=0
    while i<len(output['A']):
    	writer.writerow({'A':output['A'][i],'B':output['B'][i],'C':output['C'][i],})
    	i = i+1
