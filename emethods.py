"""Python extended methods"""

def factorial(i):
    """Given positive integer i, returns !i"""
    n = 1
    while i > 1:
        n *= i
        i -= 1
    return n
    
def triangle(i):
    """Given positive integer i, returns the triangle number with base i"""
    n = i
    while i > 1:
        i -= 1
        n += i
    return n
    
def count_possible_comparisons(l):
    """ """
    c = 0
    while l > 1:
        c += l * (l - 1)
        l -= 1
    return c
    
def count_no_overlap_neighbour_grouped_patterns(l):
    """ """
    c = 0
    
    return c

def count_no_overlap_neighbour_grouped_patterns_comparisons(l):
    """ """
    c = 0
    
    return c

def count_overlap_neighbour_grouped_patterns_comparisons(l):
    """ """
    c = 0
    while l > 1:
        c += triangle(l - 1)
        l -= 1
    return c
    
def inclusive_neighbour_pattern_division(_):
    """Given a string or array, """
    return _
    
def exclusive_neighbour_pattern_division(_):
    """ """
    return i
