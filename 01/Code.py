from collections import Counter


def readInfoText():
  infofile = open("01\test.txt", "r")
  numbers = []
  for number in infofile:
    numbers.append(int(number))
  return numbers


numbers = readInfoText()

print(numbers)
