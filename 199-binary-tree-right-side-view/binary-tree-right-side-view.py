class Solution(object):
    def rightSideView(self, r):
        if not r:
            return []
        
        a=[]
        q=deque([r])
        while q:
            for _ in range(len(q)-1):
                e=q.popleft()
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
            e=q.popleft()
            a.append(e.val)
            if e.left:
                q.append(e.left)
            if e.right:
                q.append(e.right)
        return a

        