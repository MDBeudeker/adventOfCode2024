input = "input.txt"
#input = "testinput.txt"

alist = []
blist = []

import csv
with open(input, 'r') as fd:
  reader = csv.reader(fd)
  for row in reader:
    (a,b) = (row[0].split())
    alist.append(int(a))
    blist.append(int(b))


total = 0

length = len(alist)
  
for a in range(length):
  diff = abs(min(alist) - min(blist))
  total += diff
  alist.remove(min(alist))
  blist.remove(min(blist))
  print(diff)
  print("len alist is {}".format(len(alist)))


print("final len alist is {}".format(len(alist)))

print(total)
