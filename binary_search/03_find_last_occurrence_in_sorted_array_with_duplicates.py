from typing import List


def find_last_occurrence(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    result = -1

    while left <= right:
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


arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target = 3


if find_last_occurrence(arr, target) != 4:
    raise Exception("Incorrect")
