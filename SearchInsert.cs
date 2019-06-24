public class Solution {
    public int SearchInsert(int[] nums, int target) {
        int pos = 0;
        foreach(int n in nums){
            if (n >= target){
                return pos;
            }
            pos += 1;
        }
        return pos;
    }
}