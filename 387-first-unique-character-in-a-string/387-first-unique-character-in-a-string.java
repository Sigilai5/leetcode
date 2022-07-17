class Solution {
    public int firstUniqChar(String s) {
        
        int[] alphArr = new int[26];
        String oneRepeating = new String();
    
        for(char ch: s.toCharArray()){
            alphArr[ch - 'a']++;            
        }
        
        for(char ch: s.toCharArray()){
            if(alphArr[ch - 'a'] == 1){
                oneRepeating += ch;
            }
            
    
        }
        
    
       char[] rArray = oneRepeating.toCharArray();
        
        if(rArray.length == 0){
            return -1;
        }
       
        
        char[] sArray = s.toCharArray();
        
        for(int i = 0; i < sArray.length; i++){
            if(sArray[i] == rArray[0]){
                return i;
            }else if(rArray.length == 0){
                return -1;
            }
        }
        
        
        return 0;
        
    }
}