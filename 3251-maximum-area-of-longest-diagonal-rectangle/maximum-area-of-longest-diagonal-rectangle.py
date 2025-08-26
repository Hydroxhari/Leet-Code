class Solution(object):
    def areaOfMaxDiagonal(self, d):

        ma=0
        md=0

        for i,j in d:
            cd=i*i+j*j
            if cd>=md:
                if cd==md:
                    ma=max(ma,i*j)
                else:
                    ma=i*j
                md=cd
        return ma
