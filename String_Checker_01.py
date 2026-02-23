# Check that users have entered a valid opinion based on a list

def string_checker(user_response, valid_ans):
    while True:

        # Get user response and make sure it's lowercase
        user_response = user_response.lower()

        for item in valid_ans:
            # Check if the user response is a word in the list
            if item == user_response:
                return item

            # Check if the user response is the same as the first letter of an item in the list
            elif user_response == item[0]:
                return item

        return "invalid"


# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ("Rock", "rock"),
    ("PAPER", "paper"),
    ("scissors", "scissors"),
    ("p", "paper"),
    ("S", "scissors"),
    ("XXX", "xxx"),
    ("x", "xxx"),
    ("random", "invalid"),
]

# Run tests!
for item in to_test:
    # Retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # Get actual value (ie: test ticket function)
    actual = string_checker(case, ["rock", "paper", "scissors", "xxx"])

    # Compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, recieved: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, recieved: {actual} ❌❌❌")