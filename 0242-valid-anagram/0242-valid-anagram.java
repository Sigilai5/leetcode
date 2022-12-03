class Solution {
    public boolean isAnagram(String s, String t) {   
        //Option 3
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();
        
        Arrays.sort(sArray);
        Arrays.sort(tArray);
        
        
        return Arrays.equals(sArray,tArray);
        
        
//         //*Option 2*
        
//         int[] sArray = new int[26];
//         int[] tArray = new int[26];
        
//         for(char c : s.toCharArray()){
//             sArray[c - 'a']++; 
//         }
        
        
//          for(char c : t.toCharArray()){
//             tArray[c - 'a']++;
//         }
        
//         if(Arrays.equals(sArray,tArray)){
//             return true;
//         }
        
        
//         return false;
        
        
        
        //*Option 1*
//         HashMap<Character,Integer> sCount = new HashMap();
//         HashMap<Character,Integer> tCount = new HashMap();
        
//         for(char c: s.toCharArray()){
//             sCount.put(c,sCount.getOrDefault(c,0)+1);
//         }
        
        
//         for(char c: t.toCharArray()){
//             tCount.put(c,tCount.getOrDefault(c,0)+1);
//         }
        
        
//         return sCount.equals(tCount);
        
        
        //Space Complexity->O(n+m)
        //Time Complexity->O(n+m)

    }
}


