class Solution(object):
    def reverseVowels(self, s):
        l=list(s)
        v={'a','e','i','o','u','A','E','I','O','U'}

        i=0
        j=len(s)-1
        while i<j:
            while i<j and s[i] not in v:
                i+=1
            while i<j and s[j] not in v:
                j-=1
            
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1
        return ''.join(l)


