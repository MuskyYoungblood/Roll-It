import math
import random

# Checks users enter yes (y) or no (n)

def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


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
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / "high number")
    elif low is not None and high is None:
        error = (f"Please enter an integer that is"
                 f" more than / equal to {low}")

    # if the number needs to between low & high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check response is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


# Calculate the maximum number of guesses
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses

# Main Routine Starts Here

# Initialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

game_history = []
all_scores = []

print("Welcome to the Higher Lower Game")
print()

want_instructions = string_checker("Do you want to read the instructions? ")

# Check users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ",
                       low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Ask user if they want to customise the number range
default_params = string_checker("Do you want to use the default game parameters? ")
if default_params == "yes":
    low_num = 0
    high_num = 10

# Allow user to choose the high / low number
else:
    low_num = int_check("Low Number? ")
    high_num = int_check("High Number? ", low=low_num + 1)

# Calculate the maximum number of guesses based on the low and high number
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\nRound {rounds_played + 1} (Infinite Mode)"
    else:
        rounds_heading = f"\nRound {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)

    # Round starts here
    # Set guesses used to zero at the start of each round
    guesses_used = 0
    already_guessed = []

    # Choose a 'secret' number between the low and high number
    secret = random.randint(low_num, high_num)
    print("Spoiler Alert", secret)

    guess = ""

    while guess != secret and guesses_used < guesses_allowed:

        # Ask the user to guess the number...
        guess = int_check("Guess: ", low_num, high_num, "xxx")

        # Check that they don't want to quit
        if guess == "xxx":
            # Set end_game to use so that outer loop can be broken
            end_game = "yes"
            break

        # Check that guess is not a duplicate
        if guess in already_guessed:
            print(f"You've already guessed {guess}. You've *still* used "
                  f"{guesses_used} / {guesses_allowed} guesses ")
            continue

        # If guess is not a duplicate, add it to the 'already guessed' list
        else:
            already_guessed.append(guess)

        # Add one to the number of guesses used
        guesses_used += 1

        # Compare the user's guess with the secret number set up feedback statement

        # If we have guesses left...
        if guess < secret and guesses_used < guesses_allowed:
            feedback = (f"Too low, please try a higher number. "
                        f"You've used {guesses_used} / {guesses_allowed} guesses")
        elif guess > secret and guesses_used < guesses_allowed:
            feedback = (f"Too high, please try a lower number. "
                        f"You've used {guesses_used} / {guesses_allowed} guesses")

        # When the secret number is guessed, we have three different feedback options (lucky / 'phew' / well done)
        elif guess == secret:

            if guesses_used == 1:
                feedback = "Lucky! You got it on the first guess."
                round_result = "Win"
            elif guesses_used == guesses_allowed:
                feedback = f"Phew! You got it in {guesses_used} guesses."
                round_result = "Win"
            else:
                feedback = f"Well done! You guessed the secret number in {guesses_used} guesses."
                round_result = "Win"

        # If there are no guesses left!
        else:
            feedback = "Sorry - you have no more guesses. You lose this round!"


            # penalise users for losing, score is one more than the number of guesses allowed
            guesses_used += 1

        # Print feedback to user
        print(feedback)

        # Additional Feedback (warn user that they are running out of guesses)
        if guesses_used == guesses_allowed - 1 and guesses_used == secret:
            print("\n Careful - you have one guess left! \n")

    print()

    # Round ends here

    # add guesses used to all scores list
    all_scores.append(guesses_used)

    # If user has entered exit code, end game!!
    if end_game == "yes":
        break


    rounds_played += 1

    # Add round result to game history
    history_feedback = f"Round {rounds_played}: {feedback}"
    game_history.append(guesses_used)

    # add guesses used to score list
    all_scores.append(guesses_used)

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1



# Game loop ends here

# Check users have played at least one round before calculating statistics
if rounds_played > 0:
    # Game history / statistics area

    # Calculate statistics
    all_scores.sort()

    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    # Output Game Statistics
    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"Best:{best_score} | Worst:{worst_score} | Average:{average_score:.2f} ")

    # ask user if they want to see their game history and output it if requested
    see_history = string_checker("Do you want to see the history? ")
    if see_history == "yes":
        for count, item in enumerate(game_history, start=1):
            if item <= 1:
                print(f"Round {count}: It took you {item} try to get it right!")

            else:
                print(f"Round {count}: It took you {item} tries to get it right!")


# If users have quit without playing a round, end the program gracefully.
else:
    print("🐔🐔🐔 Don't give up! 🐔🐔🐔")