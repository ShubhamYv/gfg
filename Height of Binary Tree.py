class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        return 0 if root is None else max(self.height(root.left), self.height(root.right)) + 1
