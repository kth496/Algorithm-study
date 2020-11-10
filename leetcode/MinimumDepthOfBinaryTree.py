class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        ld = self.minDepth(root.left)
        rd = self.minDepth(root.right)
        return max(ld, rd) + 1 if min(ld, rd) == 0 else min(ld, rd) + 1
