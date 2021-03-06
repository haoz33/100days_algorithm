from typing import List


# An array of boolean values is divided into two sections
# the left section consists of all false and the right section consists of all true. Find the boundary of the right section, i.e. the index of the first true element. If there is no true element, return -1.

# Input: arr = [false, false, true, true, true]

# Output: 2

# Explanation: first true's index is 2.


def find_boundary(arr: List[bool]) -> int:
    left = 0
    right = len(arr)

    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == True:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


input1 = [False, False, True, True, True]


if find_boundary(input1) != 2:
    raise Exception('Incorrect')


input2 = [False, False, False, False, False, False, True]

if find_boundary(input2) != 6:
    raise Exception('Incorrect')
