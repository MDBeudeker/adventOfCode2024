import re, csv

input = "input"
# input = "testinput"

alist = []
with open(input, 'r') as fd:
  for lines in fd:
    alist.append(lines)

print(alist)
expression=r'mul\(\d+,\d+\)'
results = []
for a in alist:
  print(type(a))
  resultsline = re.findall(expression, a)
  results.extend(resultsline) # append does not work
print(len(results))

total = 0
for result in results:
  digits = re.findall(r'\d+', result)
  digit1, digit2 = int(digits[0]), int(digits[1])
  total += digit1 * digit2
print(total)

# 25292714 is too low
# found 714 using regular search -> error -> read only 1 line, retrying
# answer 2: 161289189; correct
