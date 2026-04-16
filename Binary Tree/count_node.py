# Время выполнения: O(n)
# Память: O(h)

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

def count_nodes(node: TreeNode) -> int:
    if node is None: 
        return 0
    
    left = count_nodes(node.left)
    right = count_nodes(node.right)

    return left + right + 1

print(count_nodes(root))