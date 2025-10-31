import csv 
rows = []
with open('productos.csv', mode= 'r', newline= '') as infile:
 reader = csv.reader(infile)
  for row in reader:
    rows.append(row)


rows[2][1] = 'Updated value'

rows.append(['New Name','25','Active'])

with open ('productos_edited.csv',mode='w', newline= '') as outfile:
  writer = csv.writer(outfile)
  writer.writerows(rows)
  
