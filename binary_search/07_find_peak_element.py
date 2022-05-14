import re
from turtle import right
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if (mid == 0 or nums[mid - 1] < nums[mid]) and (mid == len(nums)-1 or nums[mid+1] < nums[mid]):
                return mid

            if nums[mid] < nums[mid-1]:
                r = mid - 1
            else:
                l = mid + 1

        if nums[0] < nums[len(nums)-1]:
            return 1
        else:
            return 0


print(Solution().findPeakElement([1, 2]))
