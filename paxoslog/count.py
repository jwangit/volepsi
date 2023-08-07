import pandas as pd
import sys
import glob
 
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
num = 0
ssize = sys.argv[1]
nn = sys.argv[2]
pre = "/home/jiale/volepsi/paxoslog/"
filename = glob.glob(pre+"nn"+nn+"-ssize"+ssize+".csv*")
head = pd.read_csv(filename[0], header=None, nrows=4, chunksize=5,on_bad_lines='skip')
for chunk in head:
  for _,row in chunk.iterrows():
    print(row[0])
data = pd.read_csv(filename[0], header=None, skiprows=4, chunksize=1000)
for chunk in data:
  for _,row in chunk.iterrows():
    length = len(row)
    if (length < 20):
      continue
    if (length > 100):
      length = 100
    for i in range(0, length):
      num += 1
      if row[i] > 0:
        count0 += 1
      if row[i] > 1:
        count1 += 1
      if row[i] > 2:
        count2 += 1
      if row[i] > 3:
        count3 += 1
      if row[i] > 4:
        count4 += 1
      if row[i] > 5:
        count5 += 1



print(">0 count:", count0)
print(">0 rate:", count0/num)
print(">1 count:", count1)
print(">1 rate:", count1/num)
print(">2 count:", count2)
print(">2 rate:", count2/num)
print(">3 count:", count3)
print(">3 rate:", count3/num)
print(">4 count:", count4)
print(">4 rate:", count4/num)
print(">5 count:", count5)
print(">5 rate:", count5/num)
