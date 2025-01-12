# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        print(root)

    def next(self) -> int:
        pass

    def hasNext(self) -> bool:
        pass

# Your BSTIterator object will be instantiated and called as such:
if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    obj = BSTIterator(root)
    param_1 = obj.next()
    param_2 = obj.hasNext()
    print(obj, param_1, param_2)