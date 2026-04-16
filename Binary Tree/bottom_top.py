# Время выполнения: O(n)
# Память: O(h)

class TreeNode:
    def  __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)

root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.left.left.left = TreeNode(5)

root.left.right = TreeNode(4)
root.left.right.right = TreeNode(6)

def find_diametr(node: TreeNode) -> int:
    diameter = 0

    def dfs(node: TreeNode) -> int:
        if node is None:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)

        nonlocal diameter
        diameter = max(diameter, left + right)

        return  max(left, right) + 1
    
    dfs(node)
    return diameter

print(find_diametr(root))