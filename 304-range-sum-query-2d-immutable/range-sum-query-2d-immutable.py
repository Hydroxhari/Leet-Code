class NumMatrix(object):

    def __init__(self, ma):
        self.m=ma
        for i in range(len(ma)):
            for j in range(1,len(ma[0])):
                self.m[i][j]+=self.m[i][j-1]

    def sumRegion(self, r1, c1, r2, c2):

        s=0
        if c1==0:
            for i in range(r1,r2+1):
                s+=self.m[i][c2]
        else:
            for i in range(r1,r2+1):
                s+=self.m[i][c2]-self.m[i][c1-1]
        return s
            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)