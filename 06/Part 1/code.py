with open(r"C:\Users\Paddi\Documents\GitHub\Advent-of-Code-2022\06\Part 1\input_test.csv") as file:
  pairs = [i for i in file.read()]

print(pairs)
print(len(pairs))

i = 0
lange = len(pairs)

for i in len(pairs):
    if i < (lange-3):
        print("iewq")
        relevant_parts = [pairs[i], pairs[i + 1], pairs[i + 2], pairs[i + 3]]
        print(relevant_parts)
        i = i+1
        print(i)

