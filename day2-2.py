import re

# Ask for our puzzle input: ULL\nRRDDD etc
print("What is your puzzle input?")

# Initialize some variables
codes = []
code = 5
x, y = 0, 2

# Create our keypad using tuples
keypad = ((None, None, 1, None, None),
          (None, 2, 3, 4, None),
          (5, 6, 7, 8, 9),
          (None, 'A', 'B', 'C', None),
          (None, None, 'D', None, None))

# Loop over the lines of instructions the user gives
while True:
    instruction = input()

    # Once they've entered all the instructions, stop looping
    if not instruction or not re.match(r"^[UDLR]+$", instruction):
        break
    
    # Loop over each individual direction within each instruction line
    for direction in instruction:

        # Get our current code by getting x,y coordinates
        # by utilizing a dictionary for makeshift Switch Case,
        # and min/max, within a generator expression, to stay in our 0-2 bounds
        (x2, y2) = tuple(min(4, max(0, i)) for i in {
            "U": (x, y - 1),
            "D": (x, y + 1),
            "L": (x - 1, y),
            "R": (x + 1, y)
        }[direction])

        # Make sure we can move that way
        if keypad[y2][x2] is None:
           continue

        (x, y) = (x2, y2)
        # Our code is in the keypad at the x,y coordinates
        code = keypad[y][x]

    # Store our final code for this line of instructions
    codes.append(code)

# Join and output our full code
print("The code is: %s" % (''.join([str(c) for c in codes])))
