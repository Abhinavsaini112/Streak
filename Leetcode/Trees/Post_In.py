class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def BuildTree(Postorder, Inorder):
    postorderIndex = len(Postorder) - 1
    inordermap = {value: index for index, value in enumerate(Inorder)}

    def helper(left, right):
        nonlocal postorderIndex

        # No nodes in this subtree
        if left > right:
            return None

        # Root is the last element in postorder
        rootValue = Postorder[postorderIndex]
        postorderIndex -= 1

        root = TreeNode(rootValue)

        inorderIndex = inordermap[rootValue]

        root.right = helper(inorderIndex + 1, right)

        root.left = helper(left, inorderIndex - 1)

        return root

    return helper(0, len(Inorder) - 1)

def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.val, end=" ")

postorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = BuildTree(postorder, inorder)

print("Postorder:")
postorderTraversal(root)