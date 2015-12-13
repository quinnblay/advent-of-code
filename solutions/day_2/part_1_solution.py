import sys

# read the input file
with open(sys.argv[1], 'r') as input_file:
    total_paper = 0

    # for every line in the input file
    for line in input_file:
        # split by the 'x' character
        measurements = line.split('x')
        # convert all the string elements to int
        measurements = map(int, measurements)
        # sort in ascending order
        measurements.sort()

        # sides
        small = measurements[0] * measurements[1]
        medium = measurements[0] * measurements[2]
        large = measurements[1] * measurements[2]

        area = (2 * small) + (2 * medium) + (2 * large) + small
        total_paper += area

    print "Total wrapping paper: " + str(total_paper) + " square feet"
