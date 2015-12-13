import sys

# read the input file
with open(sys.argv[1], 'r') as input_file:
    # assume that Santa starts at (0, 0)
    x_direction = 0
    y_direction = 0

    # store the information in a dict
    # use tuples (x,y) as key
    # initialise first present delivered at (0,0)
    presents = {(0, 0): 1}

    # for every line in the input file
    for line in input_file:
        # for every character in line
        for c in line:
            if c == '^':
                y_direction += 1
            elif c == 'v':
                y_direction -= 1
            elif c == '<':
                x_direction -= 1
            elif c == '>':
                x_direction += 1

            # visit the house
            if (x_direction, y_direction) in presents:
                presents[(x_direction, y_direction)] += 1
            else:
                presents[(x_direction, y_direction)] = 1

    print "Santa visited: " + str(len(presents)) + " houses"
