from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        

        dp = [False] * (subset_sum + 1)
        dp[0] = True

        for num in nums:
            for i in range(subset_sum, num - 1, -1):
                if dp[i]:
                    continue
                if dp[i - num]:
                    dp[i] = True
                if dp[-1]:
                    return True

        return False
    
solution = Solution()
print(solution.canPartition([1, 5, 11, 5]))