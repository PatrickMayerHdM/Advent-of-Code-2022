#Öffnen und holen des Inputs
with open("03\Part 1\input.txt") as file:
  rucksack = [i for i in file.read().strip().split("\n")]

#Erstellen Var Global
x = 0
score = 0

# Dict mit den möglichen Buchstaben incl. dem daraus folgenden Wert
Werte = {
  "a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26,
  "A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52
}

for entry in rucksack:
  #V Erstellen verschiedener Variablen für ein Durchlauf
  erster_Teil = []
  zweiter_Teil = []
  z = 0
  p = 0
  o = 0
  Z = 1

  #Herausfinden der Anzahl der Inhalte eines Rucksacks
  len_rucksack = len(rucksack[x])
  #print(len_rucksack)

  # Aufteilen des Rucksacks in einzlene (prob. useless, da man es auch einfach im Code machen kann, wenn fertig verbessern)
  One_Rucksack = rucksack[x].split()
  #print("Dieser eine Rucksack besteht aus: ", One_Rucksack, "und enthält: ", len_rucksack, "Items")

  # Aufteilen des Inhaltes eines Rucksacks in eine Liste in jeweils einem Item pro Index und aufgeteilt in zwei Compartments 
  while z < len_rucksack:
    if len(erster_Teil) < (len_rucksack/2):
      for y in One_Rucksack:
        #print(y[z])
        erster_Teil.append(y[z])
        z = z + 1
    else:
      for y in One_Rucksack:
        #print(y[z])
        zweiter_Teil.append(y[z])
        z = z + 1

  # Schauen, welcher Buchstabe in beiden vorkommt
  while p < len(erster_Teil):
    for u in erster_Teil:
      if erster_Teil[p] in zweiter_Teil and Z == 1:
        #print("YAS und der Wert beträgt:", Werte[erster_Teil[p]], "Der P Wert ist:", p )
        #print("Score in: ", score, "Score Wert: ", Werte[erster_Teil[p]], "Der Wert Z ist; ", Z)
        score = score + Werte[erster_Teil[p]]
        p = p + 1
        Z = 2
      else:
        #print("Nooo und Der P Wert ist:", p )
        p = p + 1
  
  #print(f"Der erste Teil ist: {erster_Teil} und die Länge beträgt {len(erster_Teil)}")
  #print(f"Der zweite Teil ist: {zweiter_Teil} und die Länge beträgt {len(zweiter_Teil)}")
  #print(f"Der aktuelle Score beträgt: {score}")

  x = x + 1


#print("Der Rucksack am Ende ist: ",rucksack )
print("Der Score beträgt: ", score)