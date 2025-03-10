from typing import Counter, List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount = Counter(p)
        indices = []
        l = 0
        r = len(p)
        n = len(s)
        if n < r:
            return []
        sCount = Counter(s[l:r])
        if sCount == pCount:
                indices.append(l)
        while r < n:
            l += 1
            r += 1
            if sCount[s[l-1]] > 1:
                sCount[s[l-1]] -= 1
            else:
                del sCount[s[l-1]]
            if s[r-1] in sCount:
                sCount[s[r-1]] += 1
            else:
                sCount[s[r-1]] = 1
            if sCount == pCount:
                indices.append(l)
        return indices

sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))