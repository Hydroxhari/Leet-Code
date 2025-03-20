class Solution(object):
    def trap(self, h):

        w=0
        l,r=0,len(h)-1

        lm,rm=0,0

        while l<r:
            lm=max(lm,h[l])
            rm=max(rm,h[r])

            if lm!=0 and rm!=0:
                cm=min(lm,rm)
                c=min(h[l],h[r])
                w+=cm-c
            
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        
        return w