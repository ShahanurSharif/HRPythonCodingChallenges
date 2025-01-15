from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_tree(arr: List[Optional[int]])-> Optional[TreeNode]:

    return TreeNode(arr[0])


if __name__ == '__main__':
    arr = [4, 2, 7, 1, 3, 5]
    print(generate_tree(arr))