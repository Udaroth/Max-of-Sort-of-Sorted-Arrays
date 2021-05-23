"""
Divide and Conquer to help your friend!
---------------------------------------

This is the main file where you will be modifying the program code.
Your code will be tested and marked through unit tests on Ed, your submission
will run the marking.

You ARE allowed to add your own functions, and add your own variables.
You ARE NOT allowed to modify the signature of the `get_largest_num`
function.
"""

import math

def recursion(array: list[float], arrayLen, startingIndex):

    if arrayLen == 1:
        # Only element remaining in the list
        # Return it
        return array[startingIndex]
    

    # Divide step
    # Divide the array into two halves
    halfLen = math.floor(arrayLen/2)

    # Check the first element of both arrays, and recurse on the one with the larger element.
    if array[startingIndex] > array[startingIndex+halfLen]:
        # The first half of the array should contain the largest element
        return recursion(array, halfLen, startingIndex)
    else:
        # The second half of the array should contain the largest element
        return recursion(array, arrayLen-halfLen, startingIndex+halfLen)




def get_largest_num(S: list[float]) -> float:
    """
    Return the largest number from the array S that has been incorrectly
    merge sorted. All elements in this array S are unique.
    The array takes the shape of:
    S[0] = `x-th` smallest number.
    S[1] = `(x+1)-th` smallest number.
    ...
    S[i] = `(x + i (mod N))-th` smallest number.

    :param S : The incorrectly sorted list of numbers.
    """

    # TODO implement me.
    # First of all the base case

    # Store the length of the initial array it will be used to determine 
    # n = len(S)


    return recursion(S, len(S), 0)

