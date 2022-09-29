class Solution {
    public String removeDuplicates(String s) {
       if(s.isEmpty()) return s;
       Stack<Character> stack = new Stack();  
        
       for(char c: s.toCharArray()){
           if(!stack.isEmpty() && stack.peek() == c){
               stack.pop();
           }else{
               stack.push(c);
           }
       } 
        
       String output = new String();
        
        for(char c: stack){
            output+=c;
        }
        
        return output;
        
    }
}


//Space Complexity -> O(n) since we are using a stack.
//Time Complexity -> O(n)