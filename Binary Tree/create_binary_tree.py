class TreeNode:
    def  __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(5)

root.left = TreeNode(8)
root.right = TreeNode(1)

root.left.left = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(1)