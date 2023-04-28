#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(nums):
    """ Finds the peak in a list of integers """
    if not nums:
        return None

    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return nums[left]
