import re # we use this for regex matching

# Prompt for triangle puzzle input
print("What is your puzzle input?")

# Initiate our int variables
totalTriangles = 0
trueTriangles = 0

# We'll store three triangles here at a time
temporaryTriangles = [[0] * 3, [0] * 3, [0] * 3]

# Loop over all the user input
while True:
    triangle = input()

    # Stop looping at the end of the input, or if they provide a line
    # that doesn't match the expected input format
    if not triangle or not re.match(r"^( {2,4}[0-9]{1,3}){3}$", triangle):
        break
    
    # Slice each line into its three separate sides/numbers
    (a, b, c) = tuple(int(triangle[i:i + 5]) for i in range(0, len(triangle), 5))

    # Split this current row up into the proper groupings of our 3 stored triangles
    n = totalTriangles % 3
    for i in range(3):
        temporaryTriangles[i][n] = (a, b, c)[i]

    # Keep track of how many triangles they submitted in their input
    totalTriangles += 1

    # If we've got a group of 3 triangles saved up now,
    # check if each is a true triangle by making sure the sum of
    # each possible pairing of sides is greater than the third
    if n == 2:
        trueTriangles += len([t for t in temporaryTriangles if t[0] + t[1] > t[2] and t[0] + t[2] > t[1] and t[1] + t[2] > t[0]])

# Output our answer!
print("Of the %d triangles provided, only %d are possible." % (totalTriangles, trueTriangles))
