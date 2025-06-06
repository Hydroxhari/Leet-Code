class Solution(object):
    def reverseOnlyLetters(self, s):
        
        i,j =0,len(s)-1
        s=list(s)

        while i<j:
            if s[i].isalpha() and s[j].isalpha():
                s[i],s[j]=s[j],s[i]
                i,j=i+1,j-1
            elif s[i].isalpha():
                j-=1
            else:
                i+=1
        
        return ''.join(s)


