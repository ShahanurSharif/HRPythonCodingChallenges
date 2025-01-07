# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def averageOfSubtree(self, root: TreeNode) -> int:

        def dfs(root):
            if root is None:
                return 0, 0
            left_sum, left_count = dfs(root.left)
            right_sum, right_count = dfs(root.right)
            print(left_sum, left_count, right_sum, right_count)
            subtree_sum = left_sum + right_sum + root.val
            subtree_count = left_count + right_count + 1

            if subtree_sum // subtree_count == root.val:
                nonlocal total_count
                # increment the result counter as the condition is satisfied
                total_count += 1
                # Return the sum and count of the current subtree
            return subtree_sum, subtree_count

        total_count = 0
        dfs(root)
        return total_count
        # right_sum, right_count = self.dfs(root.right)

        # avg = 0
        # return avg



if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(8)
    # root.left.left = TreeNode(0)
    # root.left.right = TreeNode(1)
    root.right = TreeNode(5)
    # root.right.right = TreeNode(6)

    solution = Solution()
    print(solution.averageOfSubtree(root))

