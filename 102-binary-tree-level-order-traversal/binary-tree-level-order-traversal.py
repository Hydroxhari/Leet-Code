class Solution(object):
    def levelOrder(self, r):
        if not r:
            return []
        
        q=deque([r])
        a=[]
        while q:
            c=[]
            for _ in range(len(q)):
                e=q.popleft()
                c.append(e.val)
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
            a.append(c)
        return a
        
