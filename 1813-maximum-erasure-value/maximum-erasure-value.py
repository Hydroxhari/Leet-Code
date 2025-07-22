class Solution(object):
    def maximumUniqueSubarray(self, n):

        s=0
        m=0
        j=0
        ss=set()
        for i in range(len(n)):
            while n[i] in ss:
                s-=n[j]
                ss.remove(n[j])
                j+=1
            s+=n[i]
            ss.add(n[i])
            m=max(m,s)
        return m