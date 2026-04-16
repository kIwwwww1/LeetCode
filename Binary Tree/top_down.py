# Время выполнения: O(n)
# Память: O(h)

class TreeNode:
    def  __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(5)

root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.left.left.left = TreeNode(5)

root.left.right = TreeNode(4)
root.left.right.right = TreeNode(6)

