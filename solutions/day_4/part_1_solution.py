import md5
import sys


# checks whether the md5 starts with 5 zeroes
def valid_md5(m):
    # get the hexdigest of the md5
    d = m.hexdigest()

    # check if valid
    for i in range(5):
        if d[i] != '0':
            return False

    return True

# our secret key
secret_key = "bgvyzdsv"

# create new default md5 object
default = md5.new()

# add the secret key
# this is the same for all of our trials
default.update(secret_key)

# start with the number 1
i = 1

while True:
    # make a copy of the default md5
    m = default.copy()

    # add the number
    m.update(str(i))

    # check if valid md5
    if valid_md5(m):
        print "Lowest number: " + str(i)
        sys.exit()
    else:
        i += 1
