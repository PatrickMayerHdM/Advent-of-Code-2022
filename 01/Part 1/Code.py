def getCalories ():
  infofile = open("01\Part 1\input.txt", "r")
  Summe = 0
  HighestSum = 0
  numbers = []
  for line in infofile:
    if line != "\n":
      numbers.append(int(line))
      Summe = Summe + int(line)
      #print("Die aktuelle Summe ist; ", Summe)
      #print("Die aktuelle Höchste Summe ist; ", HighestSum)

    else:
      if Summe > HighestSum:
        HighestSum = Summe
        Summe = 0
      else:
        Summe = 0

  return HighestSum


numbers = getCalories()

print(numbers)
