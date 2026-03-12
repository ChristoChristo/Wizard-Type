# Final Exam
# Christopher Stamulis

# Use empty print statements to create spaces and provide a greeting with instructions.
print()
print("## Lets find out what kind wizard you are!! ##")
print()
print("Answer these simple yes and no questions to learn what powers you harness within.")
print("Lets begin!")
print()

# Create a function to call and ask questions from another file. Validate user input. Then write the answers in another file to use later.

def main():
    with open("prompts", "r") as questions, open("input", "w") as answers:
        prompts = questions.read().splitlines()
        for lines in prompts:
            valid = True
            while valid:
                question = input(lines)
                if question in ["Y", "y", "N", "n"]:
                    question = question.capitalize()
                    answers.write(question)
                    valid = False
                else:
                    print("Invalid response. Please enter Y or N.\n")


print()

if __name__ == "__main__":
    main()

print()


# Create another function which utilizes the user's inputs by reading the file and then providing a response based on the total input.

def count(p, aChar):
    lettercount = 0
    for c in p:
        if c == aChar:
            lettercount = lettercount + 1
    if lettercount >= 7:
        lettercount = ("You are a the most feared WIZARD of all... the Vapormancer! \n\nA true master of the flatulent arts! \nWith the ability to propel machinery and even part the ozone layer itself, you harness your powers for good, but do not forget to excuse yourself. \nMay all part way for your aromatic ambience!")
    elif lettercount >= 4 and lettercount <= 6:
        lettercount = ("You are known as the phantom of all WIZARDS... a Mystical Dingus! \n\nThe champion of common folk, for you wield the power of all urban wall flowers united. \nMaster of holding drinks, a force to be reckoned with at any party!")
    else:
        lettercount = ("You are a WIZARD of the night...The Enchanted Goth Raver! \n\nWith your powers focused into your nostalgic light rods, you soothe the world's pain with limitless dance under the bridges of forgotten civilizations. \nA mesmerizing feet of ancient lore revitalized in the late 1990's!")
    return lettercount


with open('input', "r") as answers:
    tally = answers.read()

print (count(tally, "Y"))