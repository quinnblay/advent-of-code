import sys
import re

OFF = 0
SIZE = 1000

TURN_ON_BRIGHTNESS = 1
TURN_OFF_BRIGHTNESS = -1
TOGGLE_BRIGHTNESS = 2

### Need to +1 to all of the second number in range(_1, _2) so that it is
### inclusive of that number.


# alter the brightness by provided amount 'k'
def alter_brightness(grid, command, k):
    x1 = int(command.get('x1'))
    x2 = int(command.get('x2'))
    y1 = int(command.get('y1'))
    y2 = int(command.get('y2'))
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] = max(grid[x][y] + k, 0)

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
            # increase brightness by 1
            alter_brightness(grid, on_commands.groupdict(), TURN_ON_BRIGHTNESS)
            continue

        toggle_commands = p_toggle.match(line)
        if toggle_commands:
            # increase brightness by 2
            alter_brightness(grid, toggle_commands.groupdict(), TOGGLE_BRIGHTNESS)
            continue

        off_commands = p_off.match(line)
        if off_commands:
            # increase brightness by 1
            alter_brightness(grid, off_commands.groupdict(), TURN_OFF_BRIGHTNESS)
            continue

# total brightness in the grid
brightness = 0
for x in range(SIZE):
    for y in range(SIZE):
        brightness += grid[x][y]

print "Total brightness: " + str(brightness)
#print "Grid len x: " + str(len(grid))
#print "Grid len y: " + str(len(grid[0]))


## PRINT THE LIGHTS
#plt.imshow(grid, interpolation='nearest')
#plt.savefig('foo.png')
