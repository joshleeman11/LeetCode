class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ans = " ".join(s[::-1])
        return ans

sol = Solution()
print(sol.reverseWords("the sky is blue"))