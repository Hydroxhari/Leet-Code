class Solution(object):
    def partition(self, s):
        def pal(n):
            l,r=0,len(n)-1
            while l<r:
                if n[l]!=n[r]:
                    return False
                l+=1
                r-=1
            return True

        k=[]

        def bt(e,l):
            if e==len(s):
                k.append(l[:])
                return 
            
            for i in range(e,len(s)):
                ns=s[e:i+1]
                if pal(ns):
                    l.append(ns)
                    bt(i+1,l)
                    l.pop()
        
        bt(0,[])
        return k