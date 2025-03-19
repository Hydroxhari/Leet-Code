class Solution(object):
    def maxSlidingWindow(self, n, k):
        r=[]
        q=deque()
        l=0
        for i in range(len(n)):
            while q and n[q[-1]]<n[i]:
                q.pop()
            q.append(i)

            if l>q[0]:
                q.popleft()

            if (i+1)>=k:
                r.append(n[q[0]])
                l+=1
        return r
            
            

            
            