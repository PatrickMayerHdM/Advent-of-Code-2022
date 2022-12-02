def getCalories ():
  infofile = open("01\Part 2\input.txt", "r")
  Summe = 0
  HighestSum = 0
  SecconHighestSum = 0
  ThirdHighestSum = 0
  TopThreeElves = 0
  TopTwoElves = 0
  numbers = []
  for line in infofile:
    if line != "\n":
      numbers.append(int(line))
      Summe = Summe + int(line)
      #print("Die aktuelle Summe ist; ", Summe)
      #print("Die aktuelle Höchste Summe ist; ", HighestSum)
      #print("Die aktuell zweithöchste Summe ist: ", SecconHighestSum)
      #print("Die aktuell dritthöchste Summe ist: ", ThirdHighestSum)

    else:
      if Summe > HighestSum:
        ThirdHighestSum = SecconHighestSum
        SecconHighestSum = HighestSum
        HighestSum = Summe
        Summe = 0

      elif Summe > SecconHighestSum:
        ThirdHighestSum = SecconHighestSum
        SecconHighestSum = Summe
        Summe = 0

      elif Summe > ThirdHighestSum:
        ThirdHighestSum = Summe
        Summe = 0

      else:
        Summe = 0
  #print("Höchste Summe ist; ", HighestSum)
  #print("Zweithöchste Summe ist: ", SecconHighestSum)
  #print("Dritthöchste Summe ist: ", ThirdHighestSum)

  TopTwoElves = HighestSum + SecconHighestSum
  #print("Die zwei Top Elven haben: ", TopTwoElves)
  TopThreeElves = TopTwoElves + ThirdHighestSum

  return TopThreeElves


numbers = getCalories()
print(numbers)
