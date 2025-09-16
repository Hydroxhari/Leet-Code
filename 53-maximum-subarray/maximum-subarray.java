class Solution {
    public int maxSubArray(int[] n) {
        
        int m = -100000;
        int s = 0;

        for (int i:n){
            s+=i;
            if (i>s){
                s=i;
            }
            if (s>m){
                m=s;
            }
        }
        return m;

    }
}