with open("04\Part 1\input.txt") as file:
  pairs = [i for i in file.read().strip().split("\n")]

print(pairs)
print(pairs[0])
pair = [l.split(',') for l in ','.join(pairs).split(',')]
print(pair)