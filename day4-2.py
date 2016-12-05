import re
from collections import defaultdict

# Initialize some variables
validSectorIds = []
totalSectorIds = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def rotateLetter(letter, amount):
    # No need to mess with numbers greater than 26... reduce it down
    amount = int(amount) % 26
    letterPosition = alphabet.index(letter)

    # If rotating the letter is going to cause us to loop past Z,
    # then we can go backwards from our current position instead
    if letterPosition + amount > 25:
        return alphabet[letterPosition - (26 - amount)]
    else:
        return alphabet[letterPosition + amount]

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
    codeList = codeList[:-2]
    charList = ''.join(codeList)

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

        # We need to decrypt the name of the room and print it out
        roomName = []
        for code in codeList:
            roomName.append(''.join([rotateLetter(c, sectorId) for c in code]))
        print("%d: %s" % (int(sectorId), ' '.join(roomName)))

print("Of the %d total sector IDs provided, the sum of the %d valid sector IDs is: %d" % (totalSectorIds, len(validSectorIds), sum(validSectorIds)))
