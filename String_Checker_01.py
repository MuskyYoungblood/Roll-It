# Check that users have entered a valid opinion based on a list

def string_checker(user_response, valid_ans):
    return "yes"


# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ("yes", "yes"),
    ("Y", "yes"),
    ("No", "no"),
    ("N", "no"),
    ("YeS", "yes"),
    ("Maybe", "invalid"),
]

# Run tests!
for item in to_test:
    # Retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # Get actual value (ie: test ticket function)
    actual = string_checker(case, ["yes", "no"])

    # Compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {case}, expected: {expected}, recieved: {actual} ✅✅✅")