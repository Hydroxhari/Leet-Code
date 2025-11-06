class Solution(object):
    def maxDepth(self, r):

        if not r:
            return 0
        q=deque([r])
        c=0

        while q:
            l=len(q)
            for _ in range(l):
                n=q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            c+=1
        return c
        