from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_validate(self, root):
        if not root:
            return True

        queue = [root]
        while queue:
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
                '''
                2
                '''

            if node.right:
                queue.append(node.right)
                '''
                2
                '''



    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_validate(root)

if __name__ == '__main__':
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(2)
    q.left.right = TreeNode(3)
    q.right.left = TreeNode(3)
    '''
         2
        /\
       3  3
      /\  /\
     4  5 5 4
    '''

    solution = Solution()
    print(solution.isSymmetric(q))

