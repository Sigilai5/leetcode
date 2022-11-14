class Solution {
    public int[] twoSum(int[] numbers, int target) {
        HashMap<Integer,Integer> check = new HashMap();
        
        for(int i = 0; i < numbers.length; i++){
            int ind = target - numbers[i];
            if(check.containsKey(ind)){
                return new int[] {check.get(ind)+1,i+1};
            }
            
            check.put(numbers[i],i);
            
        }
        
        
        return numbers;
        
    }
}