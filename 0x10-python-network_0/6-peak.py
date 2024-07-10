#!/usr/bin/python3
"""test"""

def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]

    left, right = 0, n - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]

