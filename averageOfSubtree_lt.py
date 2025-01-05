# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        avg = 0
        return avg


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)

    solution = Solution()
    print(solution.averageOfSubtree(root))

