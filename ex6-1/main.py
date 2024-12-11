import csv, math

input = "input"
# input = "testinput"

alist = []
with open(input, 'r') as csv:
  content = csv.read()

def printContent(content, width, height):
  counter = 0
  for char in content:
    # print(char, end='')
    counter +=1
    if counter == width:
      print("")
      counter = 0

def rotateGuard(guard):
  if guard == '^':
    return '>'
  if guard == '>':
    return 'v'
  if guard == 'v':
    return '<'
  if guard == '<':
    return '^'
  return

def stringReplace(string, position, character):
  tempstring = string[:position] + character + string[position+1:]
  return tempstring

def checkOutOfBounds(position, nextposition, width, content):
  # check verticals
  if nextposition < 0 or nextposition > len(content):
    return True
  if ((nextposition == position + 1 ) & (nextposition % width == 0)):
    return True
  if ((nextposition == position - 1 ) & (position % width == 0)):
    return True
  else:
    return False

def moveGuard(guard, position, content, width, height):
  
  # print(position, guard)
  content = content.replace(guard,'X')
  if guard == '^':
    nextposition = position - width
  if guard == '>':
    nextposition = position + 1
  if guard == 'v':
    nextposition = position + width
  if guard == '<':
    nextposition = position - 1
  outOfBounds = checkOutOfBounds(position, nextposition, width, content)
  if outOfBounds == False:
    if (content[nextposition] == '.' or content[nextposition] == 'X'):
      content = stringReplace(content, nextposition, guard)
      position = nextposition
    elif content[nextposition] == '#':
      guard = rotateGuard(guard)
  else:
    position = nextposition
    
  return (outOfBounds, position, content, guard)
      
   

# replace line endings to work independent of unix and windows
content = content.replace("\r\n", "\n").replace("\r", "\n")

width = len(content.split("\n")[0])
height = len(content.split("\n"))
content = content.replace("\n", "")

total = 0
guard = '^'
position = content.find(guard)

counter = 0
outOfBounds= False
while outOfBounds == False:
  # print('')
  # printContent(content, width, height)
  (outOfBounds, position, content, guard) = moveGuard(guard, position, content, width, height)
  print(outOfBounds)
  counter +=1

total = content.count('X')
print("Guard {} found at position {} found {} Xes".format(guard, position, total))

# answer: 4939