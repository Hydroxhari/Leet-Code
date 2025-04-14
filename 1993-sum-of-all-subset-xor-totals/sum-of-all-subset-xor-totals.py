class Solution:
    def subsetXORSum(self, n):

        r=[]
        lr=len(n)

        def bt(s,l,a):
            if s==lr:
                r.append(a)
                return 
            r.append(a)
            for i in range(s,lr):
                l.append(n[i])
                bt(i+1,l,a^n[i])
                l.pop()
            
            return 

        bt(0,[],0)
        return sum(r)
        