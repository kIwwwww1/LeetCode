# Время выполнения: O(n)
# Память: O(h)

class TreeNode:
    def  __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(5)

root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.right = TreeNode(1)

def has_path_sum(root: TreeNode, target_sum: int) -> bool:
    def dfs(node: TreeNode, curr_sum: int) -> bool:
        if node is None:
            return False
        
        curr_sum += node.val

        if node.left is None and node.right is None:
            return curr_sum == target_sum
        
        return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
    
    return dfs(root, 0)

print(has_path_sum(root, 12))

