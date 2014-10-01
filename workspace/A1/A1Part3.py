"""
A1-Part-3: Python array indexing

Write a function that given a numpy array x, returns every Nth element in x, starting from the 
first element.  

The input arguments to this function are a numpy array x and a positive integer N such that N < number of 
elements in x. The output of this function should be a numpy array.

If you run your code with x = range(10) and N = 2, the function should return the following output: 
[0, 2, 4, 6, 8].
"""
from numpy import array

def hopSamples(x,N):
    """
    Inputs:
        x: input numpy array
        N: a positive integer, (indicating hop size)
    Output:
        A numpy array containing every Nth element in x, starting from the first element in x.
    """
    np_arr = [x[idx] for idx in range(0, len(x), N)]
    return array(np_arr)
