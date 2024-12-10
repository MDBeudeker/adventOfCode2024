import csv, math

input = "input"
# input = "testinput"

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
    if ((page.find(x) >= 0) & (page.find(y) >= 0)):
      if (page.find(x) > page.find(y)):
        valid = False
        break
  if valid:
    correctpages.append(page)

print(correctpages)
total = 0
for correctpage in correctpages:
  values = correctpage.split(",")
  midpoint = int((len(values)) / 2)
  total += int(values[midpoint])
print(total)