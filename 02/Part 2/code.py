with open("02\Part 2\input.txt") as file:
  rounds = [i for i in file.read().strip().split("\n")]

#print(rounds)
#print("Die länge der Lsite beträgt: ", len(rounds))

"""
A: opponent Rock B: opponent Paper C: opponent Scissors
X: I need to lose Y: draw Z: I need to win

Own Rock - 1 Own Paper - 2 Own Scissiors - 3
Outcome lose: 0 Outcome draw: 3 Outcome win: 6
"""

possibleOutcomes = {
  "A X":3, "A Y":4, "A Z":8,
  "B X":1, "B Y":5, "B Z":9,
  "C X":2, "C Y":6, "C Z":7,
}

i = 0
score = 0
#print(possibleOutcomes[rounds[i]])

while i < len(rounds):
  score = score + possibleOutcomes[rounds[i]]
  #print("In While Schleife ",possibleOutcomes[rounds[i]])
  i = i + 1

print(score)