with open("04\Part 2\input.txt") as file:
  pairs = [i for i in file.read().strip().split("\n")]

#print("Pairs Liste VOR for schleife: ",pairs)
included = 0
times = 0

for entry in pairs:
  first, seccond = entry.split(",")
  #print(first, seccond)
  print(times)
  
  first = [int(i) for i in first.split("-")]
  seccond = [int(i) for i in seccond.split("-")]

  if first[0] == seccond[1] or first[0] == seccond[0]:
    times = times + 1

  elif first[1] == seccond[0] or first[1] == seccond[1]:
    times = times + 1

  elif first[0] <= seccond[0] and first[1] >= seccond[1]:
    times = times + 1

  elif first[0] <= seccond[0] and first[1] <= seccond[1]:
    times = times + 1

  elif seccond[0] <= first[0] and seccond[1] >= first[1]:
    times = times + 1

  elif seccond[0] <= first[0] and seccond[1] <= first[1]:
    times = times + 1

print(times)

