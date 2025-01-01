from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        visited = [False]*len(root)
        print(visited, root)


value = [1,2,3,4,5]

root = Solution()
print(root.findLeaves(value))