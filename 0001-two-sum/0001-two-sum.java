class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] output = new int[2];
        int i = 0;
        while(i<nums.length){
            map.put(nums[i], i);
            i+=1;
        }
        
        i=0;
        while(i<nums.length){
            if(map.containsKey(target-nums[i]) && i!=map.get(target-nums[i])){
                output[0]=i;
                output[1]=map.get(target-nums[i]);
                break;
            }
            i+=1;
        }
        return output;
       
    }
}