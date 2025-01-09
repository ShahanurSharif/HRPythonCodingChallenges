from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_validate(self, root, total=[], left_val=[], right_val=[]) -> bool:
        if not root:
            return True

        queue = [root]

        while queue:
            node = queue.pop(0)
            total.append(node.val)

            if node.left:
                queue.append(node.left)
                left_val.append(node.left.val)
                '''
                2
                '''

            if node.right:
                queue.append(node.right)
                right_val.append(node.right.val)
                '''
                2
                '''
        print(total, left_val, right_val)
        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_validate(root)


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
