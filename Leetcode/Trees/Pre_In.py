class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def BuildTree(Preorder,Inorder):
    inordermap = {value : index for index,value in enumerate(Inorder)}
    preorderIndex = 0

    def helper(left,right):
        nonlocal preorderIndex
        if left > right:
            return 
        
        rootvalue = Preorder[preorderIndex]
        preorderIndex += 1

        mid = inordermap[rootvalue]

        root = TreeNode(rootvalue)

        root.left = helper(left,mid - 1)
        root.right = helper(mid + 1,right)

        return root
    
    return helper(0,len(Inorder)-1)

def preorderTraversal(root):
    if root:
        print(root.val, end=" ")
        preorderTraversal(root.left)
        preorderTraversal(root.right)


def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=" ")
        inorderTraversal(root.right)


def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.val, end=" ")


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = BuildTree(preorder, inorder)

print("Preorder:")
preorderTraversal(root)

print("\nInorder:")
inorderTraversal(root)

print("\nPostorder:")
postorderTraversal(root)

