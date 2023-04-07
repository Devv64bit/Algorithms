# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        # Perform inorder traversal and store the nodes in a list
        self.inorder(root, nodes)
        # Build a balanced binary search tree from the nodes list
        return self.buildBST(nodes, 0, len(nodes) - 1)

    def inorder(self, root, nodes):
        if not root:
            return
        self.inorder(root.left, nodes)  # Traverse left subtree
        nodes.append(root)  # Append current node to the list
        self.inorder(root.right, nodes)  # Traverse right subtree

    def buildBST(self, nodes, start, end):
        if start > end:
            return None
        mid = (start + end) // 2  # Calculate mid index
        root = nodes[mid]  # Current node will be the root of the subtree
        # Recursively build left subtree
        root.left = self.buildBST(nodes, start, mid - 1)
        # Recursively build right subtree
        root.right = self.buildBST(nodes, mid + 1, end)
        return root  # Return the root of the subtree
