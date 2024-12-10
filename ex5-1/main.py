import csv, math

# input = "input"
input = "testinput"

alist = []
with open(input, 'r') as csv:
  content = csv.read()

print(content)
content = content.replace("\r\n", "\n").replace("\r", "\n")
(rules,pages) = content.split("\n\n")

rules = rules.split("\n")
pages = pages.split("\n")

print(rules, pages)

correctpages = []

for page in pages:
  valid = True
  for rule in rules:
    (x,y) = rule.split("|")
    if ((x in page) & (y in page)):
      print("Found {} and {} in {}".format(x, y, page))
      
      # if position(x) < position(y)
      # # valid = True
      # else:
      # # valid = False
      # when all rules correct
  # if valid == True
  #   correctpages.append(page)

print(correctpages)
total = 0
for correctpage in correctpages:
  values = correctpage.split(",")
  midpoint = int((len(values)) / 2)
  print("Midpoint of {} is {}".format(correctpage, midpoint))
  print("mid value is {}".format(values[midpoint]))
  total += int(values[midpoint])
print(total)