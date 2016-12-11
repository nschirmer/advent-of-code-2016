from hashlib import md5

# Ask for our puzzle input
print("What is your puzzle input?")
door = input()

# Initialize some variables (our password var will be a list of 8 None values)
# Start i at -1 so we can increment it at the beginning of our loop this time
i = -1
password = [None] * 8

# We're going to loop over A LOT of numbers, so we'll do an endless while
while True:
    i += 1 # Increment it here since we'll be using 'continue' statements
           # which would miss this increment statement if it were at the end
    
    # Calculate our MD5 hash (door + current i value)
    doorHash = md5((door + str(i)).encode("utf-8")).hexdigest()

    # We're only interested in hashes that begin with 00000
    if doorHash[:5] == '00000':
        # We'll use a try/except to simplify things
        # If the 6th char is not a legal int, the try will fail.
        # If the 6th char (now stored in 'position') is not an index in 'password',
        # then the try will also fail. Easy way to make sure we want this position!
        try:
            position, character = int(doorHash[5]), doorHash[6]

            # If we already set a value for this position, we aren't interested
            if password[position] is not None:
                continue
        except:
            continue            

        # We now know what 'character' goes in this 'position'!
        print("Character #%d in password is '%s' based on hash: %s" % (position, character, doorHash))
        password[position] = character

        # Once we've overwrote every None value in our password list, we're done
        if None not in password:
            break

# We're using a list for password now, so turn it into a string
password = "".join(password)

print("The password for Door ID '%s' is: %s" % (door, password))
