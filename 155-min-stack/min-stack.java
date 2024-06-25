class MinStack {
    Stack<int[]> stack;

    public MinStack() {
        stack = new Stack();
    }
    
    public void push(int val) {
        if(stack.isEmpty()){
            stack.push(new int[] {val,val});
        } else{
            int lastMin = stack.peek()[1];
            stack.push(new int[] {val,Math.min(val,lastMin)});
        }
        
    }
    
    public void pop() {
        if(!stack.isEmpty()){
            stack.pop();
        }
    }
    
    public int top() {
        if(!stack.isEmpty()){
            return stack.peek()[0];
        }

        return -1;
    }
    
    public int getMin() {
        if(!stack.isEmpty()){
            return stack.peek()[1];
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
 */