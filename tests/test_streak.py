import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_all_positive_single_streak():
    assert longest_positive_streak([1, 1, 1]) == 3

def test_multiple_streaks_longest_wins():
    # two streaks: first length 2, second length 4 => answer 4
    nums = [1, 2, 0, -1, 3, 4, 5, 6, 0]
    assert longest_positive_streak(nums) == 4

def test_zeros_and_negatives_break_streaks():
    assert longest_positive_streak([2, 3, 0, 5, -1, 6, 7]) == 2
    assert longest_positive_streak([0, 0, 0]) == 0
    assert longest_positive_streak([-1, -2, -3]) == 0

def test_single_positive_returns_one():
    assert longest_positive_streak([0, -1, 5, -2]) == 1

def test_long_sequence_edge_case():
    # ensure function handles long inputs deterministically and correctly
    nums = [1] * 1000 + [0] + [1] * 500
    assert longest_positive_streak(nums) == 1000
