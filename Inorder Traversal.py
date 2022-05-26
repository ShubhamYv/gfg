class Solution:
    def InOrder(self,root):
        # code here
        arr=[]
        if not root:
            return None
        self.InOrder(root.left)
        print(root.data, end=" ")
        self.InOrder(root.right)
        return arr
