class TreeNode:
    def __init__(self,root = 0 ,left = None, right = None):
        self.root = root
        self.left = left
        self.right = right

def BuildTree(inorder,preorder):
    #hashmap to store the index of inorder values
    inorder_map = {val : idx for idx , val in enumerate(inorder)}
    pre_index = 0

    def helper(left,right):
        nonlocal pre_index

        if left > right:
            return None
        
        root_val = preorder[pre_index]
        pre_index += 1 
        
        root = TreeNode(root_val)

        index = inorder_map[root_val]

        root.left = helper(left,index - 1)
        root.right = helper(index + 1,right)

        return root
    return helper(0, len(inorder) - 1)

'''Time Complexity is O(n) and SpaceComplexity is O(n)'''

Preorder = [3,9,20,15,7]
Inorder  = [9,3,15,20,7]
result = BuildTree(Preorder,Inorder)
print(result)