class Solution(object):
    def letterCombinations(self, d):
        if not d:
            return []
        k = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }
        r=[]
        def bt(i,l):
            if i==len(d):
                r.append(''.join(l))
                return 
            
            e=d[i]
            w=k[e]

            for j in w:
                l.append(j)
                bt(i+1,l)
                l.pop()
        bt(0,[])
        return r
        
        
