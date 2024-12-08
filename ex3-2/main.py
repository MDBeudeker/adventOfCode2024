import re

input = "input"
# input = "testinput"

alist = []
with open(input, 'r') as fd:
  for lines in fd:
    alist.append(lines)

print(alist)
expression=r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
results = []
for a in alist:
  print(type(a))
  resultsline = re.findall(expression, a)
  results.extend(resultsline) # append does not work
print(len(results))

total = 0
append = True
for result in results:
  if "do()" in result:
    append = True
    print("True! {}".format(result))
  if "don't()" in result:
    print("False! {}".format(result))
    append = False
  if (("mul" in result) & append == True):
    digits = re.findall(r'\d+', result)
    digit1, digit2 = int(digits[0]), int(digits[1])
    total += digit1 * digit2
print(total)

# 83595109 is correct
