import csv

# input = "input"
input = "testinput3"

alist = []
with open(input, 'r') as csv:
  content = csv.read()

def findWord(content, word, width, height):
  np = 0
  firstLetter = word[0]

  for character in content:
    if character == firstLetter:
      positionx = np % width
      positiony = round(np / width)
      # print("Found! {} at cell {} position x {} y {}".format(firstLetter, np, positionx, positiony))
      searchLetters(content, word, np, positionx, positiony, width, height, width*height)
    np += 1
      


def searchLetters(content, word, np, positionx, positiony, width, height, size):
  total = 0
  counter = 1
  checkLeft = ((np - len(word) + 1) % width >= 0)
  checkRight = (np + len(word) + 1) % width < len(word)
  checkDown = ((np + (width * len(word)) + 1) < size)
  checkUp = ((np - (width * len(word[1:])) + 1) > 0)
  for char in word[1:]:
    #left
    if (checkLeft):
      nextValue = np-counter
      if char == content[nextValue]:
        counter += 1
        if (counter == len(word)) & (char == word[-1]):
          print("Found! {} at position {} x {} y {} going left".format(word, np, positionx, positiony))
  counter = 1
  for char in word[1:]:
    # right
    if (checkRight):
      nextValue = np+counter
      if char == content[nextValue]:
        counter += 1
        if (counter == len(word)) & (char == 'S'):
          print("Found! {} at position {} x {} y {} going right".format(word, np, positionx, positiony))
  counter = 1
  for char in word[1:]:
  # down
    if (checkDown):
      nextValue = np+(width * counter)
      # print("found X at {}; going down, next value is {}".format(np, content[np+(width * counter)]))
      if char == content[nextValue]:
        # print (char, nextValue)
        counter += 1
        if (counter == len(word)) & (char == 'S'):
          print("Found! {} at position {} x {} y {} going down".format(word, np, positionx, positiony))
  # up
  counter = 1
  for char in word[1:]:
    print("up {}".format((np - (width * len(word)) + 1)))
    if checkUp:
      nextValue= np-(width * counter)
      # print("found X at {}; going up, next value is {}".format(np, content[np-(width * counter)]))
      if char == content[nextValue]:
        # print (char, np+(width * counter))
        counter += 1
        if (counter == len(word)) & (char == 'S'):
          print("Found! {} at position {} x {} y {} going up".format(word, np, positionx, positiony))
  counter = 1
  for char in word[1:]:
    # down-right
    if checkDown & checkRight:
      nextValue = (np+(width * counter)+ counter)
      if char == content[nextValue]:
        print (char, nextValue)
        counter += 1
        if (counter == len(word)) & (char == 'S'):
          print("Found! {} at position {} x {} y {} going down-right".format(word, np, positionx, positiony))
  # up-left
  counter = 1
  for char in word[1:]:
    if checkUp & checkLeft:
      # print("found X at {}; going up-left, next value is {}".format(np, content[np-(width * counter)-counter]))
      nextValue = np-(width * counter)- counter
      if char == content[nextValue]:
        # print (char, nextValue))
        counter += 1
        if (counter == len(word)) & (char == 'S'):
          print("Found! {} at position {} x {} y {} going up-left".format(word, np, positionx, positiony))
  for char in word[1:]:
    # down-left
    if checkDown & checkLeft:
      nextValue = np+(width * counter)-counter
      if char == content[nextValue]:
        print (char, nextValue)
        counter += 1
        if (counter == len(word)) & (char == 'S'):
          print("Found! {} at position {} x {} y {} going down-left".format(word, np, positionx, positiony))
  # up-right
  counter = 1
  for char in word[1:]:
    if checkUp & checkRight:
      nextValue = np-(width * counter)+ counter
      # print("found X at {}; going up-left, next value is {}".format(np, content[np-(width * counter)-counter]))
      if char == content[nextValue]:
        # print (char, np+(width * counter))
        counter += 1
        if (counter == len(word)) & (char == 'S'):
          print("Found! {} at position {} x {} y {} going up-left".format(word, np, positionx, positiony))

    

# print(repr(content))
width = len(content.split("\n")[0])
height = len(content.split("\n"))
print(width, height)
content = content.replace("\n", "")

findWord(content, "XMAS", width, height)