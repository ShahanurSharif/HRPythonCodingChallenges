'''
Consider all the leaves of a binary tree,
from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above,
the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar
if their leaf value sequence is the same.

Return true if and only if the two given
trees with head nodes root1 and root2 are leaf-similar.



Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4],
root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false


Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].

'''
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root: Optional[TreeNode], tree_value=[]) -> Optional[list[int]]:
        if root is None:
            return []

        l, r = self.dfs(root.left), self.dfs(root.right)
        h = max(l,r)
        print(h)

        return []

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        value = self.dfs(root1, [])
        # print(value)


if __name__ == '__main__':
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    root1.right = TreeNode(1)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)

    root2 = TreeNode(3)

    solution = Solution()
    solution.leafSimilar(root1, root2)

    # root2 = TreeNode(3)
    # root2.left = TreeNode(5)
    #
