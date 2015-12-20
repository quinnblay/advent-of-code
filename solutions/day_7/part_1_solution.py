import sys
import pprint

commands = {}
results = {}

# parse input file
with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        (left, right) = line.split('->')
        # store in dictionary
        # form: wire := operations / value / etc.
        commands[right.strip()] = left.strip().split(' ')


# calculates the value assigned to a wire
def calculate(wire):
    # if wire is a number (aka just a value)
    try:
        return int(wire)
    # not a number, handle otherwise
    except ValueError:
        pass

    # check if we already know the value
    if wire not in results:
        operations = commands[wire]

        # just a value
        if len(operations) == 1:
            res = calculate(operations[0])
        else:
            # get the operator {NOT, AND, OR, LSHIFT, RSHIFT}
            op = operations[-2]
            if op == 'AND':
                res = calculate(operations[0]) & calculate(operations[2])
            elif op == 'OR':
                res = calculate(operations[0]) | calculate(operations[2])
            elif op == 'NOT':
                # remember it's supposed to be a 16-bit unsigned int
                res = ~calculate(operations[1]) & 0xffff
            elif op == 'LSHIFT':
                res = calculate(operations[0]) << int(operations[2])
            elif op == 'RSHIFT':
                res = calculate(operations[0]) >> int(operations[2])

        # add res to the results dictionary
        results[wire] = res
    # return the value assigned to the wire
    return results[wire]


# SOLVE - what signal is assigned to wire 'a'
TARGET_WIRE = 'a'
print TARGET_WIRE + ': ' + str(calculate(TARGET_WIRE))


## DEBUGGING
# Print commands
#pp = pprint.PrettyPrinter()
#pp.pprint(commands)
