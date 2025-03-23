class Solution(object):
    def maxDepth(self, r):

        if not r:
            return 0

        q=deque([r])
        l=0
        while q:
            for i in range(len(q)):
                e=q.popleft()
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
            l+=1
        return l

