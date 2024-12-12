import csv, math

input = "input"
# input = "testinput"

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

def moveGuard(guard, position, content, width, height, infiniteLoop, reflectionOCount, reflectionCount):
  
  # print(position, guard)
  if guard == '^':
    nextposition = position - width
    content = content.replace(guard,'|')
  if guard == '>':
    nextposition = position + 1
    content = content.replace(guard,'-')
  if guard == 'v':
    nextposition = position + width
    content = content.replace(guard,'|')
  if guard == '<':
    nextposition = position - 1
    content = content.replace(guard,'-')
  outOfBounds = checkOutOfBounds(position, nextposition, width, content)
  if outOfBounds == False:
    if (content[nextposition] == '.' or content[nextposition] == '|' or content[nextposition] == '-'):
      # print(guard, content[nextposition])
      if (guard =='V' or guard == '^') and content[nextposition] == '|':
          if reflectionOCount > 3:
            infiniteLoop = True
          if reflectionCount > 10000:
            infiniteLoop = True
      if (guard =='<' or guard == '>') and content[nextposition] == '-':
          if reflectionOCount > 3:
            infiniteLoop = True
          if reflectionCount > 10000:
            infiniteLoop = True
      content = stringReplace(content, nextposition, guard)
      position = nextposition
    elif (content[nextposition] == '#') or (content[nextposition] == 'O'):
      guard = rotateGuard(guard)
      reflectionCount += 1
      if content[nextposition] == 'O':
        reflectionOCount +=1
  else:
    position = nextposition
    
  return (outOfBounds, position, content, guard, infiniteLoop, reflectionOCount, reflectionCount)
      
   

# replace line endings to work independent of unix and windows
content = content.replace("\r\n", "\n").replace("\r", "\n")

width = len(content.split("\n")[0])
height = len(content.split("\n"))
content = content.replace("\n", "")

total = 0
guard = '^'
position = content.find(guard)
startposition = position
startOrientation = guard
infiniteLoopCounter = 0
startContent = content

counter = 0
countery=0

for i in range(len(content)):
  position = startposition
  guard = startOrientation
  outOfBounds = False
  infiniteLoop = False
  reflectionOCount = 0
  reflectionCount = 0
  # content = stringReplace(startContent, 2163+i, "O")
  # content = stringReplace(startContent, 2163+i, "O")
  content = stringReplace(startContent, i, "O")
  # printContent(content, width, height)
  while (outOfBounds == False) and (infiniteLoop == False):
    # print('')
    # printContent(content, width, height)
    (outOfBounds, position, content, guard, infiniteLoop, reflectionOCount, reflectionCount) = moveGuard(guard, position, content, width, height,infiniteLoop, reflectionOCount, reflectionCount)
    # printContent(content, width, height)
    counter +=1
    if infiniteLoop == True:
      print("infinite loop detected!")
      printContent(content, width, height)

      infiniteLoopCounter += 1
      # printContent(content, width, height)
    # if counter == 10000:
    #   printContent(content, width, height)
    #   exit()
  countery+=1
  print(i)
  # if countery == 2:
    # exit()
# input hangs as i = 2165

# total = content.count('|')

# total2 = content.count('-')
print("found {} infinite loops".format(infiniteLoopCounter))
# print("Guard {} found at position {} found {} |es and {} -es".format(guard, position, total, total2))

# answer: 1434