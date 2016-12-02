# Ask the user for their Puzzle Input: R2, L3, etc
print("What's your puzzle input?")
directions = input().split(', ') # Split it into an array

# Initialize our X and Y variables
x = 0
y = 0

# Initialize a compass for us to use
compass = ('North', 'East', 'South', 'West')
compassNeedle = 0

# How we'll map where we've been
mappedLocations = []

firstLocationVisitedTwice = None

# Loop over the directions we split into an array earlier
for direction in directions:
    # If we're turning to the right, we need to increase our compassNeedle by 1
    # but if it reaches 3 (the length of our 'compass' tuple, aka West)
    # then start over at 0 (North)
    if direction.startswith('R'):
        compassNeedle = {3: 0}.get(compassNeedle, compassNeedle + 1)
    # Same here. Turn to the left, decrease our compassNeedle by 1
    # Go directly to 3 (West) if we're currently facing North (0)
    else:
        compassNeedle = {0: 3}.get(compassNeedle, compassNeedle - 1)

    # Take the number of steps from the direction, by grabbing everything
    # after the first char (which we know is either R or L)
    steps = int(direction[1:])

    for i in range(steps):
        # Use a dictionary with tuples as a makeshift Switch Case...
        (x, y) = {
            'North': (x + 1, y),
            'East': (x, y + 1),
            'South': (x - 1, y),
            'West': (x, y - 1)
        }.get(compass[compassNeedle])
        
        # Check if we've been here
        if firstLocationVisitedTwice is None and (x, y) in mappedLocations:
            firstLocationVisitedTwice = (x + 0, y + 0)
        elif firstLocationVisitedTwice is None:
            # Add this location to our map, or increase the amount of times we've been there
            mappedLocations.append((x + 0, y + 0))

# Our final X and Y
print((x, y))

# Get our total steps by adding the absolute value of X and Y
print("Total steps: " + str(abs(x) + abs(y)))

print("First location visited twice: " + str(firstLocationVisitedTwice))
