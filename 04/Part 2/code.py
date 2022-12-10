with open("04\Part 2\input.txt") as file:
  pairs = [i for i in file.read().strip().split("\n")]

print("Pairs Liste VOR for schleife: ",pairs)
included = 0
times = 0

for entry in pairs:
  first, seccond = entry.split(",")
  #print(first, seccond)
  
  main_first = [int(i) for i in first.split("-")]
  main_seccond = [int(i) for i in seccond.split("-")]

  for i in pairs:

    first = [int(i) for i in first.split("-")]
    seccond = [int(i) for i in seccond.split("-")]

    print("Der Main ist: ", main_first, "Der aktuelle ist: ", first)


    

      
  print(first, seccond)
  print("Der Counter sagt: ",included)


print("So oft ist es passiert: ", included)
