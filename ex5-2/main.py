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
wrongpages = []

def swap_values(string, x ,y):
  newstring = string
  newstring = string.replace(x, "XX")
  newstring = newstring.replace(y, x)
  newstring = newstring.replace("XX", y)
  return newstring

def check_page(page, rules):
  for rule in rules:
    (x,y) = rule.split("|")
    if ((page.find(x) >= 0) & (page.find(y) >= 0)):
      if (page.find(x) > page.find(y)):
        return False
  return True

for page in pages:
  if (check_page(page, rules)):
    correctpages.append(page)
  else:
    wrongpages.append(page)


print(correctpages)
print("wrongpages before", wrongpages)

sortedwrongpages = []
# check for wrong pages
for page in wrongpages:
  newpage = page
  while check_page(newpage, rules) == False:
    for rule in rules:
      (x,y) = rule.split("|")
      if ((newpage.find(x) >= 0) & (newpage.find(y) >= 0)):
        valid = False
        while (newpage.find(x) > newpage.find(y)):
          newpage = swap_values(newpage, x,y)
          if (newpage.find(x) < newpage.find(y)):
            break
  sortedwrongpages.append(newpage)

print("sorted wrongpages ", sortedwrongpages)

total = 0
for correctpage in correctpages:
  values = correctpage.split(",")
  midpoint = int((len(values)) / 2)
  total += int(values[midpoint])
print(total)
print(sortedwrongpages)
total = 0
for sortedwrongpage in sortedwrongpages:
  values = sortedwrongpage.split(",")
  midpoint = int((len(values)) / 2)
  total += int(values[midpoint])
print(total)

# correctanswer: 5184