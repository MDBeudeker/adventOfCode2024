input = "input"
# input = "testinput"

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
counter = 0

while counter < len(alist):
  number = alist[counter]
  occurences = blist.count(alist[counter])
  total += number * occurences
  print("found {} occurences of {} in listb, bringing the total to {}".format(occurences, number, total))
  counter += 1

print("final len alist is {}".format(len(alist)))

print(total)
