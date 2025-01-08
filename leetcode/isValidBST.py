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
        queue = [root]
        previous_val = None
        is_valid = True
        while queue:

            current_node = queue.pop(0)
            previous_val = current_node.val

            if current_node.left is not None:
                if previous_val is not None and previous_val <= current_node.left.val:
                    is_valid = False
                    break
                queue.append(current_node.left)
                print('current_node= ', current_node.val, 'left= ', current_node.left.val)


            if current_node.right is not None:
                if previous_val is not None and previous_val >= current_node.right.val:
                    is_valid = False
                    break
                queue.append(current_node.right)
                print('current_node= ', current_node.val, 'right= ', current_node.right.val)

        return is_valid


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # print('hello world')
        return self.bfs_level_queue(root)


if __name__ == '__main__':
    node = TreeNode(2)
    node.left = TreeNode(2)
    node.right = TreeNode(2)
    # node.left.left = TreeNode(4)
    # node.left.right = TreeNode(5)
    # node.right.left = TreeNode(6)

    solution = Solution()
    # print(None>1)
    print(solution.isValidBST(node))