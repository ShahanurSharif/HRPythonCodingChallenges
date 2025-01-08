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
            print(len(queue))
            # print(queue[0].val, end=' ')
            total.append(queue[0].val)
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
                # if node.right is not None and node.right.val>node.val:
                #     return False
                print('node= ', node.val, 'left= ', node.left.val)


            if node.right is not None:
                queue.append(node.right)
                # if node.left is not None and node.left.val<node.val:
                #     return False
                print('node= ', node.val, 'right= ', node.right.val)


    def dfs(self, root: Optional[TreeNode], previous_value=None):
        if root is None:
            return
        getLeftNode = self.dfs(root.left, previous_value)
        getRightNode = self.dfs(root.right, previous_value)


        return True


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # print('hello world')
        value = self.bfs_level_queue(root)
        if value == False:
            return value

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