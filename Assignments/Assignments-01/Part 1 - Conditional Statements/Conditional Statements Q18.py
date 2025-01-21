# Take a user’s score and determine if they pass or fail (pass if 50 or above).

score = float(input("Enter Your Score:\n"))
if score < 50:
    print("You have failed.")
elif score >= 50 and score < 101:
    print("You have passed.")
elif score >=100:
    print("Score is between 1-100. Enter Again")

# If we don't limit the second elif then even if we enter 101 second conditional is hit
# which it shouldn't so limiting is a good idea        