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

wrongpagesnew = []
# check for wrong pages
for page in wrongpages:
  valid = False
  for rule in rules:
    (x,y) = rule.split("|")
    if ((page.find(x) >= 0) & (page.find(y) >= 0)):
      valid = False
      # do the swap values anyway, since the array consists only of wrong values. then do a while loop over all the rules again
      while (page.find(x) > page.find(y)):
        page = swap_values(page, x,y)
        if (page.find(x) < page.find(y)):
          wrongpagesnew.append(page)
          break
        # something goes wrong here, maybe we need to switch values multiple times for multpiple rules
    else:
      valid = True

print("wrongpages after", wrongpagesnew)
exit()

total = 0
for correctpage in correctpages:
  values = correctpage.split(",")
  midpoint = int((len(values)) / 2)
  total += int(values[midpoint])
print(total)
exit()
print(wrongpages)
total = 0
for wrongpage in wrongpages:
  values = wrongpage.split(",")
  midpoint = int((len(values)) / 2)
  total += int(values[midpoint])
print(total)