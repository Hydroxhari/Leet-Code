class Solution(object):
    def hasSameDigits(self, s):

        while len(s)>2:
            ns=''
            for i in range(1,len(s)):
                ns+=str((int(s[i-1])+int(s[i]))%10)
            s=ns

        return s[0]==s[1]