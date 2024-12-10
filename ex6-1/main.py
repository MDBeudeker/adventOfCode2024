import csv, math

# input = "input"
input = "testinput"

alist = []
with open(input, 'r') as csv:
  content = csv.read()

def printContent(content, width, height):
  counter = 0
  for char in content:
    print(char, end='')
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

def moveGuard(guard, position, content, width, height):
  
  print(position, guard)
  content = content.replace(guard,'X')
  if guard == '^':
    nextposition = position - width
    if content[nextposition] == '.':
      content = stringReplace(content, nextposition, '^')
      position = nextposition
    elif content[nextposition] == '#':
      guard = rotateGuard(guard)
    else:
      position = nextposition
  if guard == '>':
    nextposition = position + 1
    if content[nextposition] == '.':
      content = stringReplace(content, nextposition, '>')
      position = nextposition
    elif content[nextposition] == '#':
      guard = rotateGuard(guard)
    else:
      position = nextposition
  if guard == 'v':
    nextposition = position + width
    if content[nextposition] == '.':
      content = stringReplace(content, nextposition, 'v')
      position = nextposition
    elif content[nextposition] == '#':
      guard = rotateGuard(guard)
    else:
      position = nextposition
  if guard == '<':
    nextposition = position - 1
    if content[nextposition] == '.':
      content = stringReplace(content, nextposition, '>')
      position = nextposition
    elif content[nextposition] == '#':
      guard = rotateGuard(guard)
    else:
      position = nextposition
    
  return (position, content, guard)
      
   

# replace line endings to work independent of unix and windows
content = content.replace("\r\n", "\n").replace("\r", "\n")

width = len(content.split("\n")[0])
height = len(content.split("\n"))
content = content.replace("\n", "")

total = 0
guard = '^'
position = content.find(guard)

counter = 0
while position < (len(content) - 1):
  printContent(content, width, height)
  print('')
  (position, content, guard) = moveGuard(guard, position, content, width, height)
  counter +=1
  if counter == 15:
    exit()


print("Guard {} found at position {} found {} Xes".format(guard, position, total))

# answer: 1941