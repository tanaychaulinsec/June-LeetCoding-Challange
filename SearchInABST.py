#Iterative Solution:-

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        while root:
            if root.val>val:
                root=root.left
            elif root.val<val:
                root=root.right
            else:
                return root

#Recursive Solution:-

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        if root.val>val:
            return self.searchBST(root.left,val)
        elif root.val<val:
            return self.searchBST(root.right,val)
        else:
            return root