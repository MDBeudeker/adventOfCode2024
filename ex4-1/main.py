import csv

# input = "input"
input = "testinput"

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
      searchLetters(content, word, np, positionx, positiony, width, height)
    np += 1
      
def searchLetters(content, word, np, positionx, positiony, width, height):
  total = 0
  counter = 1
  # right
  for char in word[1:]:
    if char == content[np+counter]:
      counter += 1
      if (counter == len(word)) & (char == 'S'):
        print("Found! XMAS at position {} x {} y {} going right".format(np, positionx, positiony))
  # down
  for char in word[1:]:
    if char == content[np+(width * counter)]:
      print (char, np+(width * counter))
      counter += 1
      if (counter == len(word)) & (char == 'S'):
        print("Found! XMAS at position {} x {} y {} going down".format(np, positionx, positiony))
  # down-right
  for char in word[1:]:
    if char == content[np+(width * counter)]:
      print (char, np+(width * counter)+ counter)
      counter += 1
      if (counter == len(word)) & (char == 'S'):
        print("Found! XMAS at position {} x {} y {} going down".format(np, positionx, positiony))
  # # down-left
  # for char in word[1:]:
  #   if char == content[np+(width * counter)]:
  #     print (char, np+(width * counter)- counter)
  #     counter += 1
  #     if (counter == len(word)) & (char == 'S'):
  #       print("Found! XMAS at position {} x {} y {} going down".format(np, positionx, positiony))

#  if content[np+1] == restLetters[0]:
#    if content[np+2] == restLetters[1]:
#      if content[np+3] == restLetters[2]:
#        total += 1

    

# print(repr(content))
width = len(content.split("\n")[0])
height = len(content.split("\n"))
print(width, height)
content = content.replace("\n", "")

findWord(content, "XMAS", width, height)