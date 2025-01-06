# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node):
        if node is None:
            return 0, 0


    def averageOfSubtree(self, root: TreeNode) -> int:
        print(root)
        left_sum, left_count = self.dfs(root.left)
        right_sum, right_count = self.dfs(root.right)
        # print(left_sum, left_count)
        # avg = 0
        # return avg



if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)

    solution = Solution()
    print(solution.averageOfSubtree(root))

