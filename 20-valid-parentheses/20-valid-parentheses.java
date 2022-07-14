
class Solution {
    public boolean isValid(String s)
    {
        if(s.length() % 2 != 0) return false;
        
     Stack<Character> pStack = new Stack<Character>();
     for(char i: s.toCharArray()){
         if(i == '(' || i =='{' || i == '['){
             pStack.add(i);
         }else if( i == ')' && !pStack.isEmpty() && pStack.peek() == '('){
             pStack.pop();
         }else if( i == '}' && !pStack.isEmpty() && pStack.peek() == '{'){
             pStack.pop();
         }else if( i == ']' && !pStack.isEmpty() && pStack.peek() == '['){
             pStack.pop();
         }else{
             return false;
         }
         
     }
        
        return pStack.isEmpty();
        
        
    }
    
}
