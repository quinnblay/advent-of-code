import sys

# read the input file
with open(sys.argv[1], 'r') as input_file:
    # default floor to floor 0
    floor = 0

    # for every line in the input file
    for line in input_file:
        # for every character in the line
        for c in line:
            if c == '(':
                floor += 1
            elif c == ')':
                floor -= 1

    # print the resulting floor
    print "Floor: " + str(floor)

    # print the input file
    #print (input_file.read())
