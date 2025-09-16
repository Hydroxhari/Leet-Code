class Solution {
    public int[] twoSum(int[] n, int t) {
        int l = n.length;
        int[] ans = {0,0};
        for (int i=0;i<l;i++){
            for (int j=i+1;j<l;j++){
                if (n[i]+n[j]==t){
                    ans[0]=i;
                    ans[1]=j;
                    break;
                }
            }
        }
        return ans;
    }
}