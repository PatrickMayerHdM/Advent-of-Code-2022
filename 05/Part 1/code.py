with open("Layout.txt") as file:
    Layout = [i for i in file.read().strip().split("\n")]

print(Layout)
