# Laden der Input Daten
with open("TLayout.txt") as file:
    Layout = [i for i in file.read()]

with open("TMovements.txt") as file:
    Movement = [i for i in file.read().strip().split("\n")]

print("Dies is Layout vor bearbeitung: ",Layout)
print("Dies is Movements vor bearbeitung: ",Movement)

# Sortieren von Movement in ein dictionary
newMovement = {}
j = 0
for i in Movement:
    Num1 = i[5:6]
    Num2 = i[12:13]
    Num3 = i[17:]
    named = j

    newMovement[named] = {
        "Count": Num1,
        "From": Num2,
        "Destination": Num3
    }
    j+=1

print(newMovement[2]["Destination"])





