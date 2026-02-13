
def yes_no(question):

    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Say yes / no")

# Main Routine

want_instructions = yes_no("Do you want to see the instructions? ")
want_coffee = yes_no("Do you want coffee?" )

print("We are done")