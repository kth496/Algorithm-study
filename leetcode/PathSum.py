class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum_my(self, root: TreeNode, target: int) -> bool:
        if not root: return False

        def dfs(node: TreeNode, acc: int) -> bool:
            if not (node.left or node.right) and acc == node.val: return True
            ret = False
            if node.left:
                ret = ret or dfs(node.left, acc - node.val)
            if node.right:
                ret = ret or dfs(node.right, acc - node.val)
            return ret

        return dfs(root, target)

    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root: return False
        if root.val == target and not (root.left or root.right): return True
        return self.hasPathSum(root.left, target - root.val) or self.hasPathSum(root.right, target - root.val)
