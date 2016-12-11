import re

# Define our function that checks if a string contains an ABBA
def containsABBA(string):
    stringLen = len(string)
    # Loop over each char position in string (stopping at the 4th last char)
    for i in range(stringLen - 3):
        # Check if the char at this position is different from the char next to it
        # Then check if those two chars combined are the reverse of the next two chars

        # We're going to define our more complicated slice first
        # This slice gets the two chars that are one char away from i, reversed
        nextTwoCharsReversed = slice(i - stringLen + 3, i - stringLen + 1, -1)
        
        if string[i] != string[i+1] and string[i:i+2] == string[nextTwoCharsReversed]:
            return True

    # If we never returned True from our loop, then it's not an ABBA
    return False

# Get our puzzle input
print("What is your puzzle input?")

# Initialize some variables
ipsSupportingTLS = 0

# Loop until user is done providing input
while True:
    ip = input()

    if not ip:
        break

    # Grab all the blocks from the IP
    # Because of the way IPv7 is formatted, the hypernets will always be at odd indexes
    ipBlocks = re.findall(r"[a-z]+", ip)

    # Loop over each block
    supportsTLS = False
    for i in range(len(ipBlocks)):
        # See if this block returns True from our containsABBA function
        if containsABBA(ipBlocks[i]):
            # If the index is odd, then this was a hypernet block!
            # Hypernet containing ABBA is bad, and instantly means it's not TLS
            if i % 2:
                supportsTLS = False
                break
            supportsTLS = True
            # Even though we found out it supports TLS for this block,
            # we still have to check ALL blocks to make sure no hypernets contain ABBA

    # Increment our count
    if supportsTLS:          
        ipsSupportingTLS += 1

print("The number of IPs supporting TLS: %d" % (ipsSupportingTLS))
    
