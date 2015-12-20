import sys
import re

ON = 1
OFF = 0
SIZE = 1000

### Need to +1 to all of the second number in range(_1, _2) so that it is
### inclusive of that number.


# turn all requested lights on from command
def turn_on_lights(grid, command):
    x1 = int(command.get('x1'))
    x2 = int(command.get('x2'))
    y1 = int(command.get('y1'))
    y2 = int(command.get('y2'))
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] = ON


# turn off all request lights from command
def turn_off_lights(grid, command):
    x1 = int(command.get('x1'))
    x2 = int(command.get('x2'))
    y1 = int(command.get('y1'))
    y2 = int(command.get('y2'))
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] = OFF


# toggle all lights from command
def toggle_lights(grid, command):
    x1 = int(command.get('x1'))
    x2 = int(command.get('x2'))
    y1 = int(command.get('y1'))
    y2 = int(command.get('y2'))
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if grid[x][y] == ON:
                grid[x][y] = OFF
            else:
                grid[x][y] = ON


## check for pattern matches with p_xxx.match(line)
## get the key>value pairs with matches.groupdict() -  check if None first

# turn on
p_on = re.compile(r'^turn on (?P<x1>\d+),(?P<y1>\d+) through (?P<x2>\d+),(?P<y2>\d+)$')

# toggle
p_toggle = re.compile(r'toggle (?P<x1>\d+),(?P<y1>\d+) through (?P<x2>\d+),(?P<y2>\d+)$')

# turn off
p_off = re.compile(r'^turn off (?P<x1>\d+),(?P<y1>\d+) through (?P<x2>\d+),(?P<y2>\d+)$')

# our grid, initialising all lights to OFF
grid = [[OFF for k in range(SIZE)] for i in range(SIZE)]

with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        # check if turn on command
        on_commands = p_on.match(line)
        if on_commands:
            turn_on_lights(grid, on_commands.groupdict())
            #print "ON"
            continue

        toggle_commands = p_toggle.match(line)
        if toggle_commands:
            toggle_lights(grid, toggle_commands.groupdict())
            #print "TOGGLE"
            continue

        off_commands = p_off.match(line)
        if off_commands:
            turn_off_lights(grid, off_commands.groupdict())
            #print "OFF"
            continue

# count number of lights turned on
count = 0
for x in range(SIZE):
    for y in range(SIZE):
        if grid[x][y] is ON:
            count += 1

print "Number of lights on: " + str(count)
#print "Grid len x: " + str(len(grid))
#print "Grid len y: " + str(len(grid[0]))


## PRINT THE LIGHTS
#plt.imshow(grid, interpolation='nearest')
#plt.savefig('foo.png')
