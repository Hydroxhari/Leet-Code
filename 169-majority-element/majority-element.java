class Solution {
    public int majorityElement(int[] n) {
        int l = n.length;
        int k = l/2;
        HashMap<Integer,Integer> d = new HashMap<>();
        for (int i:n){
            d.put(i,d.getOrDefault(i,0)+1);
        }
        for (int i: d.keySet()){
            int v = d.get(i);
            if (v>k){
                return i;
            }
        }
        return 0;
    }
}