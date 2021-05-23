# Max-of-Sort-of-Sorted-Arrays


Your genius friend discovered an amazingly fast sorting algorithm using deep quantum neural networks. Unfortunately, due to complicated quantum physics beyond the scope of this unit, the algorithm's output is only sort of sorted. An array S of n integers is sort of sorted if for some  x ,   S[i] is the (x + i mod n)-th smallest number.

(Note that the 0-th smallest number is the smallest number, and the (n-1)-th smallest number is the largest number.)

Your Task
Design a divide-and-conquer algorithm that given the array S, outputs the largest number in O(log n) time.

The array S contains all unique numbers , and is incorrectly sorted as detailed above.

About the Code
dc_help.py
get_largest_num(S: List[Float]) -> Float
This is the main function, get largest num, which will be the base of your divide and conquer solution to be written.

It takes the array S, which is a list of floating point numbers, and returns the largest number in O(log N) time.


