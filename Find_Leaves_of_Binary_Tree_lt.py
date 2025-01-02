from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        def dfs(node: Optional[TreeNode], leaves: List[List[int]]) -> int:
            print(node, leaves)
            if not node:
                return -1

            left_height = dfs(node.left, leaves)
            right_height = dfs(node.right, leaves)
            print(left_height, right_height, leaves)

            curr_height = max(left_height, right_height) + 1

            if curr_height == len(leaves):
                leaves.append([])

            leaves[curr_height].append(node.val)
            return curr_height


        result = []
        dfs(root, result)
        return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    value = Solution()
    print(value.findLeaves(root))
