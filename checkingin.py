parrot = "Norweigian Blue"

letter = input("Enter your Letter")
if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("{} is not in {}".format(letter,parrot))