class Solution(object):
    def minMaxDifference(self, n):

        a=''
        b=''
        ah=''
        bh=''

        for i in str(n):
            if not ah and i!='9':
                ah=i
            if not bh and i!='0':
                bh=i
            
            if i==ah:
                a+='9'
            else:
                a+=i
            
            if i==bh:
                b+='0'
            else:
                b+=i
        
        return int(a)-int(b)
            


            
