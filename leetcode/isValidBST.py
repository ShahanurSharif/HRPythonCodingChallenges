# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bfs_level_queue(self, root: Optional[TreeNode], total=[]):
        if root is None:
            return

        queue = []
        queue.append(root)
        while len(queue)>0:
            print(queue[0].val, end=' ')
            total.append(queue[0].val)
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
                print('node= ', node, 'left= ', node.left.val)


            if node.right is not None:
                queue.append(node.right)
                print('node= ', node, 'left= ',node.right.val)


    def dfs(self, root: Optional[TreeNode], previous_value=None):
        if root is None:
            return
        getLeftNode = self.dfs(root.left, previous_value)
        getRightNode = self.dfs(root.right, previous_value)


        return True


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # print('hello world')
        self.bfs_level_queue(root)
        return True

if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)
    node.right.left = TreeNode(6)

    solution = Solution()
    print(solution.isValidBST(node))