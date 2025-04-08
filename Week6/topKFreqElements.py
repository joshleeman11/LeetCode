from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return heapq.nlargest(k, Counter(nums).keys(), key=Counter(nums).get)
    
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))