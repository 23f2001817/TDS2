"""streak.py

Deterministic, pure function to compute the longest run of consecutive
positive integers (> 0) in a list.
"""

from typing import List

__all__ = ["longest_positive_streak"]


def longest_positive_streak(nums: List[int]) -> int:
    """
    Return the length of the longest run of consecutive values strictly greater than 0.
    """
    max_streak = 0
    cur = 0
    for n in nums:
        if n > 0:
            cur += 1
            if cur > max_streak:
                max_streak = cur
        else:
            cur = 0
    return max_streak
