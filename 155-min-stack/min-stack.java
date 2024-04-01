class MinStack {
    private Stack<int[]> stack;
   
 
    public MinStack() {
        stack = new Stack();
    }
    
    public void push(int val) {
        if(stack.isEmpty()){
            int[] arr = new int[] {val,val};
            stack.push(arr);
        }else{
            int lastMin = stack.peek()[1];
            int minVal = Math.min(lastMin,val);
            int[] arr = new int[] {val,minVal};
            stack.push(arr);
        }
        
    }
    
    public void pop() {
        if(!stack.isEmpty()){
            stack.pop();
        }
               
    }
    
    public int top() {
        if(!stack.isEmpty()){
           int topElement = stack.peek()[0];
           return topElement;
        }

        return -1;
        
    }
    
    public int getMin() {
        if(!stack.isEmpty()){
            int getMin = stack.peek()[1];
            return getMin;
        }

        return -1;
        
    }
}

// SC -> O(N)
// TC -> O(1)

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 *
 **/