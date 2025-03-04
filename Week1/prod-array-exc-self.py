from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = [0]*len(nums)
        ans[0] = 1
        for i in range(1, len(nums)):
            ans[i] = ans[i-1]*nums[i-1]
        
        r = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = r * ans[i]
            r *= nums[i]

        return ans


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
