class Solution(object):
    def rightSideView(self, r):
        if not r:
            return []
        
        a=[]
        q=deque([r])
        while q:
            l=len(q)
            for i in range(len(q)):
                e=q.popleft()
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
                if i==l-1:
                    a.append(e.val)
        return a

        