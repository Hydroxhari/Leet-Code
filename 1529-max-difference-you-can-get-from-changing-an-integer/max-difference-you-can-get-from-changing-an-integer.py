class Solution(object):
    def maxDiff(self, n):

        s=str(n)

        f=False
        a= ''
        b= s[0] if s[0]!='1' else ''
        if b:
            f=True
        
        for i in s:
            if not a and i!='9':
                a=i
            if not b and i!='0' and i!=s[0]:
                b=i
        
        a=s.replace(a,'9') if  a else s
        b=s if not b else s.replace(b,'1') if f else s.replace(b,'0')
        
        print(a,b)
        return int(a)-int(b)
