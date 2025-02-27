class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def search_bst(root, target):
    """
    Given the root of a Binary Search Tree and a target value,
    return True if the target exists in the BST, False otherwise.
    
    Args:
        root: The root node of the BST (TreeNode)
        target: The target value to search for
    
    Returns:
        bool: True if target is in the BST, False otherwise
    """
    current = root
    while current:
        if target == current.val:
            return True
        elif target < current.val:
            current = current.left
        else:
            current = current.right
    return False
