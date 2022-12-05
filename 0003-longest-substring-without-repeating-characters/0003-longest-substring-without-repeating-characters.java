class Solution {
    public int lengthOfLongestSubstring(String s) {
        
     if(s.length() == 0 || s == null) return 0;    
     HashSet<Character> set = new HashSet();
        
     int left = 0;
     int right = 0;
        
     int longest = 0;
        
     while(right < s.length()){
         if(!set.contains(s.charAt(right))){
             set.add(s.charAt(right));
             longest = Math.max(longest,set.size());
             right++;
         }else{
             set.remove(s.charAt(left));
             left++;      
         }
                    
     }   
        
        
      return longest;  
        
    }
}


//Space Complexity -> O(n)
//Time Complexity -> O(n)
