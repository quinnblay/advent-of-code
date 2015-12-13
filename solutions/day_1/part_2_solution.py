import sys

# read the input file
with open(sys.argv[1], 'r') as input_file:
    # default floor to floor 0
    floor = 0

    # for every line in the input file
    for line in input_file:
        # for every character in the line - need the index so enumerate
        for index, c in enumerate(line):
            # perform the action of this command
            if c == '(':
                # go up 1 floor
                floor += 1
            elif c == ')':
                # go down 1 floor
                floor -= 1

            # check the current target floor
            if floor == -1:
                # answer!
                # need to add as problem states position starts at 1 not 0
                answer = index + 1
                print "Index: " + str(answer)

                # stop execution
                sys.exit()
