import re # we use this for regex matching

# Prompt for triangle puzzle input
print("What is your puzzle input?")

# Initiate our int variables
totalTriangles = 0
trueTriangles = 0

# Loop over all the user input
while True:
    triangle = input()

    # Stop looping at the end of the input, or if they provide a line
    # that doesn't match the expected input format
    if not triangle or not re.match(r"^( {2,4}[0-9]{1,3}){3}$", triangle):
        break

    # Keep track of how many triangles they submitted in their input
    totalTriangles += 1

    # Slice each line into its three separate sides/numbers
    (a, b, c) = tuple(int(triangle[i:i + 5]) for i in range(0, len(triangle), 5))

    # Check if it's a true triangle by making sure the sum of
    # each possible pairing of sides is greater than the third
    if a + b <= c or a + c <= b or b + c <= a:
        continue

    # If it passed our true triangle test, count it towards our final number
    trueTriangles += 1

# Output our answer!
print("Of the %d triangles provided, only %d are possible." % (totalTriangles, trueTriangles))
