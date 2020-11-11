class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ret = []
        q = deque()
        q.append((root, 1))
        if not root: return ret

        while q:
            cur, depth = q.popleft()
            if not cur: continue
            if len(ret) < depth:
                level = []
                ret.insert(0, level)
            ret[-depth].append(cur.val)
            q.append((cur.left, depth + 1))
            q.append((cur.right, depth + 1))

        return ret
