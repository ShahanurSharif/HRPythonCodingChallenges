from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            l, r = dfs(root.left), dfs(root.right)
            h = max(l, r)
            print(h, root.val)
            if len(result) == h:
                result.append([])

            result[h].append(root.val)
            return h+1

        result = []
        dfs(root)
        return result



if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    value = Solution()
    print(value.findLeaves(root))
