# Data 602 - Advanced Programming Techniques
# Kishore Prasad
# Homework 6

setup = '''

import numpy as np
import timeit
import copy

# Custom Sort
def sortwithloops(input):
    for i in range(0, len(input) - 1, 1):
         for j in range(i, len(input), 1):
             if (input[j]< input[j - 1] ):
                  tmp = input[j]
                  input[j] = input[j-1]
                  input[j-1] = tmp
    return input #return a value

# Builtin Sort
def sortwithoutloops(input):
    return sorted(input)

# Numpy Sort
def sortwithnumpy(input):
    return np.sort(input)

# Custom Search
def searchwithloops(input, value):
    for i in range(0, len(input), 1):
        if(input[i] == value):
            return 'TRUE'
    return 'FALSE'

# Builtin Search
def searchwithoutloops(input, value):
    if value in input:
        return 'TRUE'
    return 'FALSE'

# Numpy Search
def searchwithnumpy(input, value):
    return "False" if np.size(np.where(input == value)) == 0 else "True"

# Setup the test subjects
np.random.seed(123)

# Smaller test subject with 100 items
l_100 = np.random.randint(0, 5000, size=100)
nl_100 = np.array(l_100)

# Larger test subject with 1000 items
l_1000 = np.random.randint(0, 2000, size=1000)
nl_1000 = np.array(l_1000)

'''

# Number of times to execute the timed test
n = 10000

# Execute the Sort test for smaller test subject and print the results
t1_l_100 = timeit.timeit("x=copy.copy(l_100); sortwithloops(x)", setup=setup, number=n)
t2_l_100 = timeit.timeit("x=copy.copy(l_100); sortwithoutloops(x)", setup=setup, number=n)
t3_nl_100 = timeit.timeit("x=copy.copy(nl_100); sortwithnumpy(x)", setup=setup, number=n)


print("""
Sort function with 100 items for 10000 loops

Using loops            : {0:.5f} sec
Using built in python  : {1:.5f} sec
Using numpy            : {2:.5f} sec

""".format(t1_l_100, t2_l_100, t3_nl_100))


# Execute the Search test for smaller test subject and print the results
t1_l_100 = timeit.timeit("x=copy.copy(l_100); searchwithloops(x, 12)", setup=setup, number=n)
t2_l_100 = timeit.timeit("x=copy.copy(l_100); searchwithoutloops(x, 12)", setup=setup, number=n)
t3_nl_100 = timeit.timeit("x=copy.copy(nl_100); searchwithnumpy(x, 12)", setup=setup, number=n)


print("""
Search function with 100 items for 10000 loops

Using loops            : {0:.5f} sec
Using built in python  : {1:.5f} sec
Using numpy            : {2:.5f} sec

""".format(t1_l_100, t2_l_100, t3_nl_100))


# Number of times to execute the timed test
n = 1000

# Execute the Sort test for larger test subject and print the results
t1_l_1000 = timeit.timeit("x=copy.copy(l_1000); sortwithloops(x)", setup=setup, number=n)
t2_l_1000 = timeit.timeit("x=copy.copy(l_1000); sortwithoutloops(x)", setup=setup, number=n)
t3_nl_1000 = timeit.timeit("x=copy.copy(nl_1000); sortwithnumpy(x)", setup=setup, number=n)


print("""
Sort function with 1000 items for 1000 loops

Using loops            : {0:.5f} sec
Using built in python  : {1:.5f} sec
Using numpy            : {2:.5f} sec

""".format(t1_l_1000, t2_l_1000, t3_nl_1000))


# Execute the Search test for smaller test subject and print the results
t1_l_1000 = timeit.timeit("x=copy.copy(l_1000); searchwithloops(x, 12)", setup=setup, number=n)
t2_l_1000 = timeit.timeit("x=copy.copy(l_1000); searchwithoutloops(x, 12)", setup=setup, number=n)
t3_nl_1000 = timeit.timeit("x=copy.copy(nl_1000); searchwithnumpy(x, 12)", setup=setup, number=n)


print("""
Search function with 1000 items for 1000 loops

Using loops            : {0:.5f} sec
Using built in python  : {1:.5f} sec
Using numpy            : {2:.5f} sec

""".format(t1_l_1000, t2_l_1000, t3_nl_1000))


