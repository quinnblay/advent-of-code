import md5
import sys


# checks whether the md5 starts with n zeroes
def valid_md5(n, m):
    # get the hexdigest of the md5
    d = m.hexdigest()

    # check if valid
    for i in range(int(n)):
        if d[i] != '0':
            return False

    return True

# get number of leading zeroes to be found
n = sys.argv[1]

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
    if valid_md5(n, m):
        print "Lowest number: " + str(i)
        sys.exit()
    else:
        i += 1
