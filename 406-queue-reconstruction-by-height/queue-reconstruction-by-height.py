class Solution(object):
    def reconstructQueue(self, p):
        
        p.sort(key = lambda x:(-x[0],x[1]))

        l=[]
        for i in p:
            l.insert(i[1],i)
        return l