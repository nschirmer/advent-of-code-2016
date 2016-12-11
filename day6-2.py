from collections import defaultdict
import operator

# Get our puzzle input
print("What is your puzzle input?")

# Initialize our variable, which'll be a list of dicts, but we're not sure of the length yet
characters = None

# Keep getting user input until no more input is provided
while True:
    message = input()

    if not message:
        break

    # Initialize our characters variable for real, which'll only run the very first time
    # We're setting it to a list of dicts, and we're saying anytime we try to access a key that doesn't exist,
    # that key should be initialized as an int (which'll of course start at 0).
    # The length of our list is the length of the first line of input.
    if characters is None:
        characters = [defaultdict(int) for i in range(len(message))]

    # Loop over each char in the message line, and increment how many times that char has been seen
    # for each position
    i = 0
    for c in message:
        characters[i][c] += 1
        i += 1

# This is a rather long/messy list expression...
# It loops over each dict of chars for the length of our message,
# then reverse-sorts those dict of chars by their value (number of times used),
# then grabs the next (first) iteration from that dict, which will be our char used most,
# then grabs the key from the (key, value) tuple returned by next()
# Yeah, sorry.
# DAY 6 PART 2 NOTE: Literally the only thing we had to change was removing reverse=True from our sorted() arguments
errorCorrectedMessage = "".join([next(iter(sorted(chars.items(), key=operator.itemgetter(1))))[0] for chars in characters])

print("The error-corrected message is: %s" % (errorCorrectedMessage))
