input = "input"
# input = "testinput"

alist = []

import csv
with open(input, 'r') as fd:
  reader = csv.reader(fd)
  for row in reader:
    alist.append(row[0].split())

total, check = 0, 0

def safetyCheck(report):
  counter = 0
  firstnumber, lastnumber = int(report[0]), int(report[-1])
  if firstnumber > lastnumber:
    direction = -1
  elif firstnumber < lastnumber:
    direction = 1
  else:
    return False
  for data in report:
    if counter > 0:
        aold = a
        a = int(data)
        print (aold, a, (direction * (a - aold))) 
        if (0 < (direction * (a - aold)) <= 3):
          safe = True
        else:
          safe = False
          break
    elif counter == 0:
      a = int(data)
      counter += 1

  print ("report {} is safe: {}".format(report, safe))
  return safe



counter = 0
 #expect 585
for report in alist:
  # set safe to False
  safe = False
  safe = safetyCheck(report)
  counter += 1
  if safe == True:
    total += 1

print(total)
print(check)