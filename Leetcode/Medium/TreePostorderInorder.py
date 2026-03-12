class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTree(root):
    if not root:
        return
    print(root.val, end=" ")
    printTree(root.left)
    printTree(root.right)

'''Postorder -> [left,right,root] and Inorder -> [left,root,right]'''
'''Time Complexity is O(n) and Space Complexity is O(n)'''

def BuildTree(postorder, inorder):

    # hashmap to store index of inorder values
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    
    post_index = len(postorder) - 1

    def helper(left, right):
        nonlocal post_index
        
        if left > right:
            return None
        
        # root value from postorder
        root_val = postorder[post_index]
        post_index -= 1
        
        root = TreeNode(root_val)

        # find root in inorder
        index = inorder_map[root_val]

        # IMPORTANT: build right subtree first
        root.right = helper(index + 1, right)
        root.left = helper(left, index - 1)

        return root

    return helper(0, len(inorder) - 1)

Postorder = [9,15,7,20,3]
Inorder  = [9,3,15,20,7]
result = BuildTree(Postorder,Inorder)
printTree(result)
