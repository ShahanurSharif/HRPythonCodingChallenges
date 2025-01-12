from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_mirror(self, left_val: TreeNode, right_val: TreeNode) -> bool:
        print(left_val, right_val)
        if not left_val and not right_val:
            return True
        if not left_val or not right_val:
            return False

        return (left_val.val == right_val.val and
                self.is_mirror(left_val.left, right_val.right) and
                self.is_mirror(left_val.right, right_val.left))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.is_mirror(root.left, root.right)


if __name__ == '__main__':
    q = TreeNode(2)

    q.left = TreeNode(3)
    q.right = TreeNode(3)

    q.left.left = TreeNode(4)
    q.left.right = TreeNode(5)
    q.right.left = TreeNode(5)
    q.right.right = TreeNode(4)

    q.left.left.left = TreeNode(6)
    q.left.left.right = TreeNode(7)
    q.left.right.left = TreeNode(8)
    q.left.right.right = TreeNode(9)

    q.right.left.left = TreeNode(9)
    q.right.left.right = TreeNode(8)
    q.right.right.left = TreeNode(7)
    q.right.right.right = TreeNode(6)

    '''
    
                 2
            /        \
           3           3
          / \        /   \
         4   5      5      4
        / \ / \    / \    / \
       6  7 8  9  9   8  7   6
       
    '''

    solution = Solution()
    print(solution.isSymmetric(q))
