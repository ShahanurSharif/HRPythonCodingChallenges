# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bfs_level_queue(self, root: Optional[TreeNode], total=[]) -> bool:
        if root is None:
            return
        queue = []
        queue.append(root)
        previous_node = None
        return_value = True
        while len(queue)>0:
            if previous_node is not None and previous_node > queue[0].val:
                return_value = False
                break

            node = queue.pop(0)
            previous_node = node.val

            if node.left is not None:
                queue.append(node.left)
                print('node= ', node.val, 'left= ', node.left.val)


            if node.right is not None:
                queue.append(node.right)
                print('node= ', node.val, 'right= ', node.right.val)

        return return_value


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # print('hello world')
        return self.bfs_level_queue(root)


if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.left.left = TreeNode(4)
    node.left.right = TreeNode(5)
    node.right.left = TreeNode(6)

    solution = Solution()
    # print(None>1)
    print(solution.isValidBST(node))