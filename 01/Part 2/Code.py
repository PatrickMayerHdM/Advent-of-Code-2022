from collections import Counter


def readInfoText():
  infofile = open("01\input.txt", "r")
  Summe = 0
  HighestSum = 0
  numbers = []
  for line in infofile:
    if line != "\n":
      numbers.append(int(line))
      Summe = Summe + int(line)
      print("Die Summe ist ", Summe)
      print("Die aktuell höchste Summe ist ", HighestSum)
      
    else:
      if Summe > HighestSum:
        HighestSum = Summe
        Summe = 0
      else:
        Summe = 0

  return numbers


numbers = readInfoText()

print(numbers)
print(sum(numbers))
