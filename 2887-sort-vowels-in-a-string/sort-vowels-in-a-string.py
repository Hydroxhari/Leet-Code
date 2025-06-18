class Solution(object):
    def sortVowels(self, s):

        k='AEIOUaeiou'

        l=['']*len(s)
        d=defaultdict(int)
        for i in range(len(s)):
            if s[i] not in k:
                l[i]=s[i]
            else:
                d[s[i]]+=1
        
        r=[[i,j] for i,j in d.items()]
        r.sort()

        for i in range(len(s)):
            if l[i]=='':
                l[i]=r[0][0]
                r[0][1]-=1
                if r[0][1]==0:
                    r.pop(0)

        return ''.join(l)



