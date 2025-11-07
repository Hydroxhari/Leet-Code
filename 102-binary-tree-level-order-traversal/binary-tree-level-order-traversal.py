class Solution(object):
    def levelOrder(self, r):

        a=[]
        if not r:
            return []
        q=deque([r])
        while q:
            l=len(q)
            b=[]
            for _ in range(l):
                e=q.popleft()
                b.append(e.val)
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
            a.append(b)
        return a