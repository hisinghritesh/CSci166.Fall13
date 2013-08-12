import csv
def test_print(file):
   with open(file, 'rb') as f:
       reader = csv.reader(f)
       for row in reader:
           print row
   f.close()

def test_read(file):
   f = open(file, 'rb')
   o = []
   reader = csv.reader(f)
   for row in reader:
      o.append([int(i) for i in row])
   return o

def avg_rows(mat):
   avg = []
   for row in mat:
      r_avg = 0
      for i in row:
         r_avg += i
      avg.append(r_avg/len(row))
   return avg

out = test_read('some.csv') 
out_avg = avg_rows(out)




