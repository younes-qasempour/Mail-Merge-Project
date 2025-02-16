with open("./Input/Letters/starting_letter.txt") as f:
    letter_content = f.readlines()

with open("./Input/Names/invited_names.txt") as f:
    names_content = f.readlines()

names = []
for name in names_content:
    names.append(name.strip())

letter = ""
for line in letter_content:
    letter = letter + line

for name in names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as f:
        f.write(letter.replace("[name]", name))
