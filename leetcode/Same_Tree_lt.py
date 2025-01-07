from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs_preOrder(self, tree, tree_value=[]):

        if tree is None:
            tree_value.append(None)
            return tree_value

        self.dfs_preOrder(tree.left, tree_value)
        self.dfs_preOrder(tree.right, tree_value)
        tree_value.append(tree.val)
        return tree_value

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        p_value = self.dfs_preOrder(p, [])
        # print(p_value)
        q_value = self.dfs_preOrder(q, [])

        # print(p_value, q_value)

        if p_value != q_value:
            return False

        return True



if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    sol = Solution()
    print(sol.isSameTree(p, q))