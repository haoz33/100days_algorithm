from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        index = -1
        while low <= high:
            mid = (low+high)//2

            if matrix[mid][0] <= target <= matrix[mid][len(matrix[mid]) - 1]:
                index = mid
                break

            if matrix[mid][0] < target:
                low = mid + 1
            elif matrix[mid][len(matrix[mid])-1] > target:
                high = mid - 1

        if index == -1:
            return False

        left = 0
        right = len(matrix[index])-1

        arr = matrix[index]

        while left <= right:
            mid = (left+right)//2

            if arr[mid] == target:
                return True

            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


# print(Solution().searchMatrix(
#     [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(Solution().searchMatrix(
    [[1, 3]], 3))
