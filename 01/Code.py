from collections import Counter


def readInfoText():
  infoFile = open("01\test.txt", "r")
  numbers = []
  for number in infoFile:
    numbers.append(int(number))
  return numbers

numbers = readInfoText()
print(numbers)