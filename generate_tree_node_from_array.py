from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_tree(arr: List[Optional[int]])-> Optional[TreeNode]:
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i=0
    while i < len(arr):
        current = queue.pop(0)
        '''
        left = 2 * i + 1 
        right = 2 * i + 2
        '''

        if i<len(arr) and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)

        i += 1

        if i<len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)

        i += 1

    return root


if __name__ == '__main__':
    arr = [1, 2, 3, None, 5, 6, 7]
    root = generate_tree(arr)


    # Function to print the tree (for testing purposes).
    def print_tree(root):
        if not root:
            return
        queue = [root]
        result = []
        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append(None)
        print(result)


    print_tree(root)