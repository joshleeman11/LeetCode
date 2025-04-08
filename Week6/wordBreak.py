from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

    def word_break(self, s: str) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            if i == 0 or dp[i - 1]:
                curr = self.root
                for j in range(i, len(s)):
                    c = s[j]
                    if c not in curr.children:
                        break

                    curr = curr.children[c]
                    if curr.is_word:
                        dp[j] = True
        return dp[-1]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        root = Trie()
        for word in wordDict:
            root.insert(word)
        
        return root.word_break(s)
    
sol = Solution()
print(sol.wordBreak("leetcode", ["leet", "code"]))