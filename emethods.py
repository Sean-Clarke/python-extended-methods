"""Python extended methods"""

def mysort(l):
    """Sorts the given list l"""
    srt = [i for i in range(len(l) - 1)]
    while srt != []:
        if l[srt[0]] > l[srt[0] + 1]:
            l[srt[0]], l[srt[0] + 1] = l[srt[0] + 1], l[srt[0]]
            if srt[0] != 0:
                srt.append(srt[0] - 1)
        srt = srt[1:]

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
    
def count_comparisons(l):
    """Given length l, returns the number of comparisons needed to compare every two values in a list of size l with each other"""
    c = 0
    while l > 1:
        c += l * (l - 1)
        l -= 1
    return c
    
def count_matches(array):
    """Given array array, returns the number of """
    count = 0
    for index in range(len(array)):
        for comparison in array[index + 1:]:
            if array[index] == comparison:
                count += 1
                break
        
    return count
    
def distinct_matches(array):
    """Given array array, returns a dictionary of key value pairs matching unique items in array and their number of occurences in array"""
    count = 0
    dictionary = {}
    for item in array:
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary
    
def count_instances(m, array):
    """Given m and array array, returns the number of instances of m in array"""
    count = 0
    for item in array:
        if item == m:
            count += 1
    return count
    
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
    
def prime(i):
    """Given positive integer i, returns boolean value of prime identity"""
    if i != 2 and i % 2 == 0:
        return False
    for n in range(3, int(i**0.5) + 1, 2):
        if i % n == 0:
            return False
    return True

def nth_prime(n):
    """Given positive integer n, returns the nth prime"""
    pass
    return
    
def next_prime(i):
    """Given integer i, returns the lowest prime greater than i"""
    if i % 2 == 0:
        i += 1
    else:
        i += 2
    lesser_primes=[]
    for n in range(3, int(i**0.5) + 1, 2):
        add = True
        for p in lesser_primes:
            if n % p == 0:
                add = False
                break
        if add == True:
            lesser_primes.append(n)
    found = False
    while not found:
        found = True
        for p in lesser_primes:
            if i % p == 0:
                found = False
                i += 2
                break
    return i
"""    
def n_primes(n, start=2):
    """#Given integer n, integer start, returns an array of size n populated with an increasing sequence of primes greater than or equal to start
    """
    primes = []
    if start != 2:
        lp = primes_between(2, int(start**0.5))
    else:
        lp = []
    if prime(start):
        primes.append(start)
        n -= 1
    while n > 0:
        if len(lp) > 0 and lp[-1] <= int(start**0.5) + 1:
            lp.append(next_prime(lp[-1], lesser_primes=[pn for pn in lp if pn <= lp[-1]**0.5 + 1]))
        start = next_prime(start, lesser_primes=lp)
        primes.append(start)
        n -= 1
    return primes
"""
def primes_between(start, end):
    """Given integer start and integer end, returns a list of all primes between start and end"""
    pass
    return
