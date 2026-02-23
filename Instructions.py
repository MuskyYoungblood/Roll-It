
def yes_no(question):
    while True:
        response = input(question).lower()

        # Checks user response, question
        # Repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Say yes / no")

# Displays instructions

def instruction():
