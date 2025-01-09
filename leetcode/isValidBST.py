# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bfs_level_queue(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True # an empty tree consider a valid BST

        queue = [(root, float('-inf'), float('inf'))]
        # print(queue)
        while queue:
            node, lower, upper = queue.pop(0)

            if not lower<node.val<upper:
                return False

            if node.left:
                queue.append((node.left, lower, node.val))

            if node.right:
                queue.append((node.right, node.val, upper))

        return True
                # 1, -inf, 2




    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # print('hello world')
        return self.bfs_level_queue(root)


if __name__ == '__main__':
    node = TreeNode(2)
    node.left = TreeNode(1)
    node.right = TreeNode(3)
    # node.left.left = TreeNode(4)
    # node.left.right = TreeNode(5)
    # node.right.left = TreeNode(6)

    solution = Solution()
    print(solution.isValidBST(node))