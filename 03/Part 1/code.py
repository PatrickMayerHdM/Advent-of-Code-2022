with open("03\Part 2\input.txt") as file:
  rucksack = [i for i in file.read().strip().split("\n")]
x = 0

for entry in rucksack:
  len_rucksack = len(rucksack[x])
  print(len_rucksack)

  first = [i for i in first.read().strip().split(len_rucksack)]
  print(first)

  x = x + 1

  


print(rucksack)