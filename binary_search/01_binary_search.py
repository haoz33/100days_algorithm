from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left+right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


input1 = [-1, 0, 3, 5, 9, 12]

if search(input1, 9) != 4:
    raise Exception('Incorrect')


input2 = [-1, 0, 3, 5, 9, 12]
if search(input2, 2) != -1:
    raise Exception('Incorrect')
