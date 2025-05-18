class Solution(object):
    def insert(self, l, n):
        l.append(n)
        l.sort()

        q = []
        q.append(l[0])

        for i in l[1:]:
            x = q[-1][1]
            s,e = i[0],i[1]

            if s<=x:
                q[-1][1] = max(x,e)
            else:
                q.append(i)
        
        return q
        