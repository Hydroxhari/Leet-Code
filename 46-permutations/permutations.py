class Solution(object):
    def permute(self, n):

        ls=[]
        
        def bt(l,v):
            if len(v)==len(n):
                ls.append(l)
                return
            
            for i in n:
                if i not in v:
                    v.add(i)
                    bt(l+[i],v)
                    v.remove(i)
            
        bt([],set())
        return ls