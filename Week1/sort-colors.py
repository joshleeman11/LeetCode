from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums) - 1
        curr = 0

        while curr <= p2:
            if nums[curr] == 0:
                tmp = nums[p0]
                nums[p0] = nums[curr]
                nums[curr] = tmp
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                tmp = nums[p2]
                nums[p2] = nums[curr]
                nums[curr] = tmp
                p2 -= 1
            elif nums[curr] == 1:
                curr += 1


sol = Solution()
nums = [2, 0, 2, 1, 1, 0]
sol.sortColors(nums)
print(nums)
