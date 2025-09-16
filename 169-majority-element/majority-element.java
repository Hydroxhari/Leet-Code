class Solution {
    public int majorityElement(int[] n) {
        int l = n.length;
        int k = l/2;
        Arrays.sort(n);
        int p=-1;
        int c=0;
        for (int i:n){
            if (p==-1 || i==p){
                c++;
                if (c>k){
                    return i;
                }
            }
            else{
                c=1;
                p=i;
            }
        }
        return 0;
    }
}