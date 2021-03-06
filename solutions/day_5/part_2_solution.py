import sys
import re

# pattern 1 - at least 3 vowels (aeiou) - check for 3x later
#p_vowels = re.compile('[aeiou]')

# pattern 2 - a letter appears twice in a row
#p_row = re.compile('(\\w)\\1')

# pattern 3 - none of these: ab, cd, pq, or xy
#p_strings = re.compile('(ab)|(cd)|(pq)|(xy)')

# pattern 1 - pair of 2 letters > appears twice
p_pairs = re.compile('(..).*\\1')

# pattern 2 - one letter that repeats with another in between
p_repeats = re.compile('(.).\\1')

# read the input file
with open(sys.argv[1], 'r') as input_file:
    nice_count = 0

    # for every line in the input file
    for line in input_file:
        # check for at least 3 vowels
        if len(p_pairs.findall(line)) < 1:
            continue  # failed first test

        # check for a letter twice in a row
        if len(p_repeats.findall(line)) < 1:
            continue  # failed second test

        nice_count += 1

    print "Number of nice strings: " + str(nice_count)
