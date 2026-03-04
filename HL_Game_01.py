import math

# Checks users enter yes (y) or no (n)

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


def instruction():
    print('''

**** Instructions ****

To begin, choose the number of rounds and either customise
the game parameters or go with the default game (where the
secret number will be between 1 and 100).

Then choose how many rounds you'd like to play <enter> for
infinite mode.

Your goal is to try to guess the secret number without
running out of guesses.

Good luck.

    ''')

# Checks for an integer with optional upper / lower limits and an optional exit code for infinite mode / quitting the game
def int_check(question, low=None, high=None, exit_code=None):

# Calculate the maximum number of guesses
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses

# Checks for an integer more than 0 (allow <enter>)

def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # Check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # Checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main Routine Starts Here

# Initialise game variables
mode = "regular"
rounds_played = 0

print("Welcome to the Higher Lower Game")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

# Check users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ",
                       low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Get Game Parameters
low_num = int_check("Low Number? ")
high_num = int_check("High Number? ", low=low_num + 1)
guesses_allowed = calc_guesses(low_num, high_num)
# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\nRound {rounds_played + 1} (Infinite Mode)"
    else:
        rounds_heading = f"\nRound {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)
    print()

    user_choice = input("Choose: ")


    # If user choice is the exit code, break the loop
    # if user_choice == "xxx":
    #    break


    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1



# Game loop ends here

# Game history / statistics area