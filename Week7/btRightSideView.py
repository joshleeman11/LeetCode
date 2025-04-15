# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: 
        if root is None:
            return []
        result = []
        queue = deque([root])

        while queue:

            right_side = None
            for _ in range(len(queue)):

                curr = queue.popleft()

                if curr:
                    right_side = curr
                    queue.append(curr.left)
                    queue.append(curr.right)
               
            if right_side:
                result.append(right_side.val)
        return result




