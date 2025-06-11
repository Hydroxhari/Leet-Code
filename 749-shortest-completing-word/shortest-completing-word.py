class Solution(object):
    def shortestCompletingWord(self, l, w):
        
        a=[]
        for i in l:
            if i.isalpha():
                a.append(i.lower())
        
        d=Counter(a)
        
        r=''

        for i in w:
            if Counter(i)&d==d:
                if not r:
                    r=i
                else:
                    if len(r)>len(i):
                        r=i
        
        return r


