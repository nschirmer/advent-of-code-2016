import re
from collections import defaultdict

# Initialize some variables
validSectorIds = []
totalSectorIds = 0

print("What is your puzzle input?")

# Loop over all the lines the user pasted
while True:
    encryptedCode = input()

    if not encryptedCode:
        break

    # Initialize some dicts with expected default values
    countsByChar = defaultdict(int)
    charsByCount = defaultdict(list)

    # Cut our code line up into all the pieces.
    # Like split('-') except it grabs the [checksum] too
    codeList = re.findall(r"[a-z0-9]+", encryptedCode)
    if not codeList:
        continue

    # Keep a record of how many we've gone through
    totalSectorIds += 1

    # We know the sector ID and checksum are the last two in the string
    (sectorId, checksum) = codeList[-2:]
    # The rest are the chars we have to count up
    charList = ''.join(codeList[:-2])

    # Get a record of how many times each char appears
    for c in charList:
        countsByChar[c] += 1

    # Take the above dict and flip it around... so {a: 1, b: 1, c: 3} would be {1: [a, b], 3: [c]}
    [charsByCount[count].append(char) for char, count in countsByChar.items()]

    # Take the new above dict, sort it by the key (which is our count), and join the letters together, and slice by 5
    expectedCode = ''.join([''.join(sorted(chars)) for count, chars in sorted(charsByCount.items(), reverse=True)])[:5]

    #print("Expected code: %s" % (expectedCode))
    #print("Provided code: %s" % (checksum))

    # If the checksum matches, it's a valid sector ID
    if checksum == expectedCode:
        validSectorIds.append(int(sectorId))

print("Of the %d total sector IDs provided, the sum of the %d valid sector IDs is: %d" % (totalSectorIds, len(validSectorIds), sum(validSectorIds)))
