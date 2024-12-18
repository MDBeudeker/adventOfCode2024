import csv, math

input = "input"
# input = "testinput"

alist = []
with open(input, 'r') as csv:
  content = csv.read()

def findWord(content, word, width, height, total):
  np = 0
  firstLetter = word[1]

  for character in content:
    if character == firstLetter:
      positionx = ((np ) % width) + 1
      positiony = math.ceil((np+1)/width)
      # print("Found! {} at cell {} position x {} y {}".format(firstLetter, np, positionx, positiony))
      total = total + searchLetters(content, word, np, positionx, positiony, width, height, width*height)
    np += 1
  return total
      


def searchLetters(content, word, np, positionx, positiony, width, height, size):
  total = 0
  checkLeft = (positionx - 1 > 0)
  checkRight = (positionx + 1 <= width)
  checkDown = ((positiony + 1 <= height))
  checkUp = ((positiony - 1) >= 0)
  answer = []
  # down-right
  if checkDown & checkRight:
    nextValue = (np+(width)+ 1)
    if content[nextValue] == 'S' or content[nextValue] == 'M':
      answer.append(content[nextValue])
  # down-left
  if checkDown & checkLeft:
    nextValue = np+(width)-1
    if content[nextValue] == 'S' or content[nextValue] == 'M':
      answer.append(content[nextValue])
  # up-left
  if checkUp & checkLeft:
    nextValue = np-(width)- 1
    if content[nextValue] == 'S' or content[nextValue] == 'M':
      answer.append(content[nextValue])
  # up-right
  if checkUp & checkRight:
    nextValue = np-(width)+1
    if content[nextValue] == 'S' or content[nextValue] == 'M':
      answer.append(content[nextValue])
  if answer == ['M', 'M', 'S', 'S'] or answer == ['S', 'M', 'M', 'S'] or answer == ['S', 'S', 'M', 'M'] or answer == ['M', 'S', 'S', 'M']:
    print("Found MAS at position {}, positionx {} positiony {}".format(nextValue, positionx, positiony))
    total +=1
  return total

    

# replace line endings to work independent of unix and windows
content = content.replace("\r\n", "\n").replace("\r", "\n")

width = len(content.split("\n")[0])
height = len(content.split("\n"))
content = content.replace("\n", "")

total = 0
total = findWord(content, "MAS", width, height, total)
print("Total: {}".format(total))

# answer: 1941