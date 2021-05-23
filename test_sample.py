"""
Simple tests to help you see if you are doing your algorithm correctly.
"""

import timeit
import unittest

import dc_help


def get_next_n(start: float = 0, stop: float = 0, inc: float = 1):
    num = float(start)
    while True:
        yield num
        num += inc
        if num >= stop:
            break


class TestMyCodePlease(unittest.TestCase):

    def test_code_example(self):

        original_list = [1, 2, 3, 4, 5]
        shift = 2
        maxnum = 5

        S = original_list[shift:] + original_list[:shift]

        # Correctness
        res = dc_help.get_largest_num(S)

        assert res == maxnum, \
            f"Expected {maxnum} but got {res}"

    def test_complexity(self):

        original_list = [n for n in get_next_n(1, 148939, 2)]

        shift = 5
        maxnum = original_list[-1]

        S = original_list[shift:] + original_list[:shift]

        # Correctness
        res = dc_help.get_largest_num(S)

        assert res == maxnum, \
            f"Expected {maxnum} but got {res}"

        timed_func = timeit.timeit(
            lambda: dc_help.get_largest_num(S),
            number=500)

        print(f"Your calls took {timed_func}s")
