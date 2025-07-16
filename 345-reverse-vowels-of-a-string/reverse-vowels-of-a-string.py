class Solution(object):
    def reverseVowels(self, s):
        l=list(s)
        i,j=0,len(s)-1
        v={'a','e', 'i', 'o','u'}
        while i<j:
            if s[i].lower() in v and s[j].lower() in v:
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
            elif s[i].lower() in v:
                j-=1
            elif s[j].lower() in v:
                i+=1
            else:
                i+=1
                j-=1
        return ''.join(l)


