input = "input"
# input = "testinput"

alist = []

import csv
with open(input, 'r') as fd:
  reader = csv.reader(fd)
  for row in reader:
    alist.append(row[0].split())

total, check = 0,0


for report in alist:
  # set safe to False
  safe = False
  counter = 0
  dampenerUsed = False
  # check whether decreasing
  if int(report[0]) > int(report[-1]):
    for data in report:
      if counter == 0:
        a = int(data)
        counter += 1
      else:
        aold = a
        a = int(data)
        print (aold, a) 
        if (0 < (aold - a) <= 3):
          safe = True
        elif dampenerUsed == False:
          dampenerUsed = True
          print ("counter = {}".format(counter))
          print ("dampener used on {}".format(a))
          a = aold
        else :
          safe = False
          break
  # when increasing
  if int(report[0]) < int(report[-1]):
    for data in report:
      if counter == 0:
        a = int(data)
        counter += 1
      else: 
        aold = a
        a = int(data)
        print (aold, a) 
        if (0 < (a - aold) <= 3):
          safe = True
        elif dampenerUsed == False:
          dampenerUsed = True
          print ("counter = {}".format(counter))
          print ("dampener used on {}".format(a))
          a = aold
        else :
          safe = False
          break
  # edge case: start and end are the same = safe is False by default
  if int(report[0]) == int(report[-1]):
    check += 1
    safe = False
  print ("report {} is safe: {}".format(report, safe))


  if safe == True:
    total += 1

print(total)
print(check)

## 615 is too low
## 668 is too high