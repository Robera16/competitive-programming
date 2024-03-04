class Solution {
    public int countPairs(List<Integer> nums, int target) {
        Collections.sort(nums);
        int left = 0;
        int right = nums.size() - 1;
        int output = 0;
        
        while(left < right){
            if(nums.get(left)+nums.get(right) < target){
                output+= (right-left);
                left+=1;
            }
            else{
                while(right >=0 && nums.get(left)+nums.get(right) >= target){
                    right-=1;
                }
            }
        }
        
        return output;
        
    }
}