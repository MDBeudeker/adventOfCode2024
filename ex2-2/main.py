input = "input"
# input = "testinput"

alist = []

import csv
with open(input, 'r') as fd:
  reader = csv.reader(fd)
  for row in reader:
    alist.append(row[0].split())

total, check = 0, 0

def safetyCheck(report, debug=0):
  counter = 0
  firstnumber, lastnumber = int(report[0]), int(report[-1])
  
  # determine whether report is ascending or descending
  if firstnumber > lastnumber:
    # descending
    direction = -1
  elif firstnumber < lastnumber:
    # ascending
    direction = 1
  else:
    # neither -> return False
    return False
  
  # iterate through report
  for data in report:
    if counter > 0:
        aold = a
        a = int(data)
        # if debug == 1:
        #   print (aold, a, (direction * (a - aold)))
        if (0 < (direction * (a - aold)) <= 3):
          safe = True
        else:
          safe = False
          break
    elif counter == 0:
      a = int(data)
      counter += 1

  if debug == 1:
    print ("report {} is safe: {}".format(report, safe))
  return safe

def dampen(report):
  print("result for report {} is false, trying to dampen".format(report))
  for i in range(len(report)):
    dampenedReport = report[:i] + report[i+1:]  # Remove the i-th element
    if safetyCheck(dampenedReport):
        print("received safe result for report {} by dampening {}".format(report, report[i]))
        return True
  return False
    


for report in alist:
  # set safe to False
  safe = False
  safe = safetyCheck(report)
  if safe == True:
    total += 1
  else:
    # if result is safe attempt to dampen
    safe = dampen(report)
    if safe == True:
      total += 1

print(total)
print(check)

## 615 is too low
## 624 is too low
## 625 is too low
## 668 is too high