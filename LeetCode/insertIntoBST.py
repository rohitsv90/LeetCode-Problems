# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        new_node = TreeNode(val)
        if root is None:
            root = new_node
        else:
            if val < root.val:
                if root.left is not None:
                    self.insertIntoBST(root.left, val)
                else:
                    root.left = new_node
            else:
                if root.right is not None:
                    self.insertIntoBST(root.right, val)
                else:
                    root.right = new_node
        return root
            