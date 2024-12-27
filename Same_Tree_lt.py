from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if len(p) != len(q):
        #     return False
        print(p, q)

        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(4)))