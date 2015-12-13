import sys

# read the input file
with open(sys.argv[1], 'r') as input_file:
    total_ribbon = 0

    # for every line in the input file
    for line in input_file:
        # split by the 'x' character
        measurements = line.split('x')
        # convert all the string elements to int
        measurements = map(int, measurements)
        # sort in ascending order
        measurements.sort()

        # perimeter
        perimeter = 2 * (measurements[0] + measurements[1])
        # ribbon is all the measurements multiplied together
        ribbon = reduce(lambda x, y: x*y, measurements)

        total_ribbon += perimeter + ribbon

    print "Total ribon: " + str(total_ribbon) + " feet"
