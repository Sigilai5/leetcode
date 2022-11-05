class Solution {
    public int maxPower(String s) {
        int max = 1;
        int tempCount = 1;
        
        char[] sArray = s.toCharArray();
        
        for(int i = 1; i<sArray.length;i++){
            if(sArray[i] == sArray[i-1]){
                tempCount++;
                max = Math.max(max,tempCount);
            }else{
                tempCount = 1;
            }
            
        }
        
        
        return max;
        
    }
        
}


//Time Complextiy -> O(N)
//Space Complexity -> O(1)