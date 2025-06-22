class Solution:
    def divideString(self, s: str, k: int, f: str) -> List[str]:

        l=len(s)
        if l%k!=0:
            s+=f*(k-(l%k))
            
        r=[]
        for i in range(0,l,k):
            r.append(s[i:i+k])
        return r
