with open("input.txt") as file:
  pairs = [i for i in file.read().strip().split("\n")]

print("Pairs Liste VOR for schleife: ",pairs)
included = 0
times = 0

for entry in pairs:
  first, seccond = entry.split(",")
  #print(first, seccond)
  
  first = [int(i) for i in first.split("-")]
  seccond = [int(i) for i in seccond.split("-")]

  if first[0] <= seccond[0] and first[1] >= seccond[1]:
      included = included + 1
      times += 1

  elif seccond[0] <= first[0] and seccond[1] >= first[1]:
      #print("Bin in der zweiten auch drin")
      included = included + 1
      times += 1

  else:
    pass
      
  #print(first, seccond)
  #print("Der Counter sagt: ",included)

#print("So oft ist es durchgelafen: ", times)
print("So oft ist es passiert: ", included)
