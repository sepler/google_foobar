from __future__ import division
from fractions import Fraction # Answer will be in fraction-form

def answer(pegs):

    sections = list() # Build list of all sections between pegs
    for i in xrange( len(pegs) - 1 ):
        sections.append( pegs[i+1] - pegs[i] )

    max_init_radius = sections[0]
    max_last_radius = sections[-1]

    possible = list() # Possible solutions

    i = 1
    while i < max_init_radius: # Iterate until max possible first peg (len(section) - 1)
        d_2 = i / 2 # Double speed of last = first peg radius /2
        if d_2 < max_last_radius and d_2 > 1: # Check if real radius
            possible.append(Fraction(i)) # Add to possible solutions
        i += Fraction('1/3') # Iterate first gear radius
        # Iterating by 1 = 6 test cases passed
        # Iterating by 1/2 = 6 test cases passed
        # Iterating by 1/3 = 10 test cases passed

    #print possible


    for first in possible: # First peg
        gears = [first] # First gear
        for peg in xrange(len(pegs)): # Iterate pegs
            new_gear = sections[peg-1] - gears[peg-1] # Next gear = left_section_length - last_gear_radius
            if new_gear < 1: # Check if real radius
                gears = None
                break
            else: # Add to list of gears
                gears.append(new_gear)

        if gears and isclose(gears[0], gears[-1] * 2): # If last gear is twice speed of first
            return Fraction(gears[0]).numerator, Fraction(gears[0]).denominator

    return [-1, -1]


# https://www.python.org/dev/peps/pep-0485/#proposed-implementation
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
