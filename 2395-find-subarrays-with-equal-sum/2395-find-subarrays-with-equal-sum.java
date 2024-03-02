class Solution {
    public boolean findSubarrays(int[] nums) {
        int i = 0;
        boolean output = false;
        HashMap<Integer, Integer>map = new HashMap<>();
        
        while (i<nums.length-1){
            if(map.containsKey(nums[i]+nums[i+1])){
                output = true;
                break;
            } else {
                map.put(nums[i]+nums[i+1], i);
            }
            i+=1;
        }
        return output;
    }
}