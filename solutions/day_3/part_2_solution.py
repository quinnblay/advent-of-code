import sys

# read the input file
with open(sys.argv[1], 'r') as input_file:
    # assume that Santa and Robo start at (0, 0)
    santa_x = 0
    santa_y = 0
    robo_x = 0
    robo_y = 0

    # store the information in a dict
    # use tuples (x,y) as key
    # initialise first 2 presents (Santa and Robo) delivered at (0,0)
    presents = {(0, 0): 2}

    # Santa goes first
    santa_turn = True

    # for every line in the input file
    for line in input_file:
        # for every character in line
        for c in line:
            # process the action
            if c == '^':
                if santa_turn:
                    santa_y += 1
                else:
                    robo_y += 1
            elif c == 'v':
                if santa_turn:
                    santa_y -= 1
                else:
                    robo_y -= 1
            elif c == '<':
                if santa_turn:
                    santa_x -= 1
                else:
                    robo_x -= 1
            elif c == '>':
                if santa_turn:
                    santa_x += 1
                else:
                    robo_x += 1

            # visit the house
            if santa_turn:
                if (santa_x, santa_y) in presents:
                    presents[(santa_x, santa_y)] += 1
                else:
                    presents[(santa_x, santa_y)] = 1
            else:
                if (robo_x, robo_y) in presents:
                    presents[(robo_x, robo_y)] += 1
                else:
                    presents[(robo_x, robo_y)] = 1

            # change turn
            santa_turn = not santa_turn

    print "Santa and Robo visited: " + str(len(presents)) + " houses"
