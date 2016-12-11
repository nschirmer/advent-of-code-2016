from hashlib import md5

# Ask for our puzzle input
print("What is your puzzle input?")
door = input()

# Initialize some variables
i = 0
password = ""

# We're going to loop over A LOT of numbers, so we'll do an endless while
while True:
    # Calculate our MD5 hash (door + current i value)
    doorHash = md5((door + str(i)).encode("utf-8")).hexdigest()

    # We're only interested in hashes that begin with 00000
    if doorHash[:5] == '00000':
        # The next character in 'password' is the 6th character in the hash
        print("Next character in password is '%s' based on hash: %s" % (doorHash[5], doorHash))
        password += doorHash[5]

        # Once our password reaches 8 characters in length, we're done
        if len(password) == 8:
            break

    # Need to make sure we increment this or our while loop will be truly endless
    i += 1

print("The password for Door ID '%s' is: %s" % (door, password))
