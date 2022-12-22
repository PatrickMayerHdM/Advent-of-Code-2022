#Öffnen und holen des Inputs
with open("03\Part 1\input.txt") as file:
  rucksack = [i for i in file.read().strip().split("\n")]

Len_ges_rucksack = len(rucksack)
print(f"dass ist Rucksack {rucksack} mit der Länge: {Len_ges_rucksack}")

#Erstellen Var Global
x = 0
score = 0
entry = 0

# Dict mit den möglichen Buchstaben incl. dem daraus folgenden Wert
Werte = {
  "a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26,
  "A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52
}

for entry in rucksack:
  #print("Das ist entry",entry)
  #V Erstellen verschiedener Variablen für ein Durchlauf
  if x + 2 > Len_ges_rucksack:
    pass

  else:
    RucksackDetail = []
    RucksackDetail_Two = []
    RucksackDetail_Three = []
    z = 0
    Found = False


    #länge Rucksack
    len_r1 = len(rucksack[x])
    len_r2 = len(rucksack[x+1])
    len_r3 = len(rucksack[x+2])

    #print("Die Länge von 3",len_r3)
    # Aufteilen des Rucksacks in einzlene (prob. useless, da man es auch einfach im Code machen kann, wenn fertig verbessern)
    One_Rucksack = rucksack[x].split()
    Two_Rucksack = rucksack[x + 1].split()
    Three_Rucksack = rucksack[x + 2].split()

    #print("Der beobachtete Rucksack besteht aus: ", One_Rucksack, "und enthält: ", len_rucksack, "Items, dazu kommen noch die beiden folgenden Rucksäcke ", Two_Rucksack, (len(rucksack[x+1])),  Three_Rucksack, (len(rucksack[x+2])))

    # Aufteilen des Inhaltes eines Rucksacks in eine Liste in jeweils einem Item pro Index
    while z < len_r1:
      for y in One_Rucksack:
        RucksackDetail.append(y[z])
        z = z + 1

    z = 0
    while z < len_r2:
      for y in Two_Rucksack:
        RucksackDetail_Two.append(y[z])
        z = z + 1
    
    z = 0
    while z < len_r3:
      for q in Three_Rucksack:
        RucksackDetail_Three.append(q[z])
        z = z + 1
    
    #print("Der beobachtete Rucksack besteht aus: ", RucksackDetail,"dazu kommen noch die beiden folgenden Rucksäcke ", RucksackDetail_Two, RucksackDetail_Three)

    z = 0
    #Schauen welcher Index in den nächsten 3 vorkommt

    while z + 2 < len(rucksack[x]):
      for y in One_Rucksack:
        print(f"Der Gesamt Score beträgt (vor dem Durchlauf des Buchstabens {RucksackDetail[z]}) beträgt: ", score)
        if RucksackDetail[z] in RucksackDetail_Two and RucksackDetail[z] in RucksackDetail_Three and Found == False:
          score = score + Werte[RucksackDetail[z]]
          print(f"Der aktuelle Buchstabe ist {RucksackDetail[z]} und der dazugehörige Score ist: {Werte[RucksackDetail[z]]}")
          z = z + 1
          Found = True
        else:
         z = z + 1

    print(f"Der Rucksack im Detail ist: {RucksackDetail} und die Länge beträgt {len(RucksackDetail)}")
    #print(f"Der aktuelle Score beträgt: {score}")

    x = x + 3


  


#print("Der Rucksack am Ende ist: ",rucksack )
print("Der Score beträgt: ", score)