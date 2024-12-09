import csv

# input = "input"
input = "testinput"

alist = []
with open(input, 'r') as csv:
  content = csv.read()

def findWord(content, word, width, height, total):
  np = 0
  firstLetter = word[0]

  for character in content:
    if character == firstLetter:
      positionx = np % width
      positiony = round(np / width)
      # print("Found! {} at cell {} position x {} y {}".format(firstLetter, np, positionx, positiony))
      total = total + searchLetters(content, word, np, positionx, positiony, width, height, width*height)
    np += 1
  return total
      


def searchLetters(content, word, np, positionx, positiony, width, height, size):
  total = 0
  checkLeft = ((np - len(word) + 1) % width >= 0)
  checkRight = (np + len(word) + 1) % width < len(word)
  checkDown = ((np + (width * len(word)) + 1) < size)
  checkUp = ((np - (width * len(word[1:])) + 1) > 0)
  #left
  counter = 1
  for char in word[1:]:
    if (checkLeft):
      nextValue = np-counter
      if char == content[nextValue]:
        counter += 1
        if (counter == len(word)) & (char == word[-1]):
          print("Found! {} at position {} x {} y {} going left".format(word, np, positionx, positiony))
          total +=1
  # right
  counter = 1
  for char in word[1:]:
    if (checkRight):
      nextValue = np+counter
      if char == content[nextValue]:
        counter += 1
        if (counter == len(word)) & (char == 'S'):
          print("Found! {} at position {} x {} y {} going right".format(word, np, positionx, positiony))
          total +=1
  # down
  counter = 1
  for char in word[1:]:
    if (checkDown):
      nextValue = np+(width * counter)
      # print("found X at {}; going down, next value is {}".format(np, content[np+(width * counter)]))
      if char == content[nextValue]:
        # print (char, nextValue)
        counter += 1
        if (counter == len(word)) & (char == 'S'):
          print("Found! {} at position {} x {} y {} going down".format(word, np, positionx, positiony))
          total +=1
  # up
  counter = 1
  for char in word[1:]:
    # print("up {}".format((np - (width * len(word)) + 1)))
    if checkUp:
      nextValue= np-(width * counter)
      # print("found X at {}; going up, next value is {}".format(np, content[np-(width * counter)]))
      if char == content[nextValue]:
        # print (char, np+(width * counter))
        counter += 1
        if (counter == len(word)) & (char == 'S'):
          print("Found! {} at position {} x {} y {} going up".format(word, np, positionx, positiony))
          total +=1
  # down-right
  counter = 1
  for char in word[1:]:
    if checkDown & checkRight:
      nextValue = (np+(width * counter)+ counter)
      # deze checken, index out of range
      print("going down-right at x {} y {}, next value is {}".format(positionx, positiony, content[nextValue]))
      if char == content[nextValue]:
        print (char, nextValue)
        counter += 1
        if (counter == len(word)) & (char == 'S'):
          print("Found! {} at position {} x {} y {} going down-right".format(word, np, positionx, positiony))
          total +=1
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
          total +=1
  # down-left
  counter = 1
  for char in word[1:]:
    if checkDown & checkLeft:
      nextValue = np+(width * counter)-counter
      # if nextValue < size:
      #   break
      print("xposition: {} yposition: {} nextValue: {} size: {}".format(positionx, positiony, nextValue, size))
      print((np - len(word) + 1) % width)
      print((np + (width * len(word)) + 1))
      print(nextValue)
      # deze checken, index out of range
      if char == content[nextValue]:
        print (char, nextValue)
        counter += 1
        if (counter == len(word)) & (char == 'S'):
          print("Found! {} at position {} x {} y {} going down-left".format(word, np, positionx, positiony))
          total +=1
  # up-right
  counter = 1
  for char in word[1:]:
    if checkUp & checkRight:
      nextValue = np-(width * counter)+ counter
      # print("found X at {}; going up-right, next value is {}".format(np, content[np-(width * counter)-counter]))
      if char == content[nextValue]:
        # print (char, np+(width * counter))
        counter += 1
        if (counter == len(word)) & (char == 'S'):
          print("Found! {} at position {} x {} y {} going up-right".format(word, np, positionx, positiony))
          total +=1
  return total

    

# replace line endings to work independent of unix and windows
content = content.replace("\r\n", "\n").replace("\r", "\n")

width = len(content.split("\n")[0])
height = len(content.split("\n"))
print(width, height)
content = content.replace("\n", "")

total = 0
total = findWord(content, "XMAS", width, height, total)
print("Total: {}".format(total))