from typing import List


# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


# Find the first index, and then first the last index

# When encountered a target value, we need to determine whatever it is first or last or middle


def searchRange(nums: List[int], target: int) -> List[int]:
    result = [-1, -1]

    result = [find_first_occurrence(
        nums, target), find_last_occurrence(nums, target)]

    return result


def find_first_occurrence(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
            continue

        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return result


def find_last_occurrence(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    result = -1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1
            continue

        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return result


input1 = [5, 7, 7, 8, 8, 10]
target1 = 8
result1 = [3, 4]


input2 = [5, 7, 7, 8, 8, 10]
target2 = 6
result2 = [-1, -1]


if searchRange(input1, target1) != result1:
    raise Exception("first example incorrect")


if searchRange(input2, target2) != result2:
    raise Exception("second example incorrect")
