class Solution {
    public boolean checkDistances(String s, int[] distance) {
        
        HashMap<Character,Integer> map = new HashMap<>();
        int i = 0;
        char c;
        boolean output = true;
        
        while(i<s.length()){
            c=s.charAt(i);
            if(map.containsKey(c)){
                map.put(c, i-map.get(c)-1);
            } else {
                map.put(c, i);
            }
            i+=1;
        }
        // System.out.println(map);
        for(HashMap.Entry<Character,Integer> entry : map.entrySet()){
            // System.out.println(entry.getKey()+" "+entry.getValue());
            if(distance[(int)entry.getKey()-97]!=entry.getValue()){
                output=false;
                break;
            }
        }
        return output;
    }
}