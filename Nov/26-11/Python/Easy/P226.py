# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        if root == []:
            return None
        def invert_node(node):
            if not node:
                return None
            temp = node.left
            node.left = node.right
            node.right = temp
            invert_node(node.left)
            invert_node(node.right)
            return node


        return invert_node(root)

            
        