with open("04\Part 1\input.txt") as file:
  pairs = [i for i in file.read().strip().split("\n")]

print("Pars Liste VOR for schleife: ",pairs)

for entry in pairs:
  first, seccond = entry.split(",")
  #print(first, seccond)
  
  first = [int(i) for i in first.split("-")]
  seccond = [int(i) for i in seccond.split("-")]

  print(first,seccond)
  print("Split")
  print(first)
print(pairs)