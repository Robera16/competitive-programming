class Solution {
    public int findMaxK(int[] nums) {
        Arrays.sort(nums);
        HashMap<Integer,Integer> map = new HashMap<>();
        int output=-1;
        // System.out.println(Arrays.toString(nums));
        for(int i=0; i<nums.length; i++){
            // System.out.print(num);
            if(nums[i]<0){
                map.put(nums[i],i);
            }else{
                if(map.containsKey(-nums[i])){
                    output=nums[i];
                }
            }
        }
        return output;
    }
}