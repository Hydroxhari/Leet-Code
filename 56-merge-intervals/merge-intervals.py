class Solution(object):
    def merge(self, n):
        n.sort(key = lambda x:x[0])

        s=[n[0]]
        for i in n[1:]:
            a,b=i
            if a<=s[-1][1]:
                s[-1][1]=max(s[-1][1],b)
            else:
                s.append([a,b])
        return s
            
