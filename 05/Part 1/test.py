# Open the file "TLayout.txt" and read its contents
with open("TLayout.txt", "r") as file:
    layout_txt = file.read()

# Splitte das Layout in Zeilen
lines = layout_txt.strip().split('\n')
print(lines)

# Initialisiere eine Liste, um die verkettete Liste zu speichern
linked_list = []

# Iteriere durch jede Zeile und erstelle die verkettete Liste
for i, line in enumerate(lines):
    # Entferne führende und abschließende Leerzeichen, dann teile in Zeichen auf
    characters = line.strip().split()

    # Füge die Zeichenliste der verketteten Liste hinzu
    linked_list.append(characters)

# Erstelle das gewünschte Ergebnis
result = {}
print(linked_list)
for i, characters in enumerate(linked_list):
    result[i + 1] = characters

print(result)