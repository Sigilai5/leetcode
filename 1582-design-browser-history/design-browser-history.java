class BrowserHistory {
    List<String> pages;
    int current;

    public BrowserHistory(String homepage) {
        this.pages = new ArrayList<>();
        this.pages.add(homepage);
        this.current = 0;        
    }
    
    public void visit(String url) {
        while(this.pages.size() - 1 != this.current){
            this.pages.remove(this.pages.size() - 1);
        }

        this.pages.add(url);
        this.current+=1;
    }
    
    public String back(int steps) {
        this.current = Math.max(0,this.current - steps);
        return this.pages.get(this.current);
        
    }
    
    public String forward(int steps) {
        this.current = Math.min(this.pages.size() - 1,this.current + steps);
        return this.pages.get(this.current);
        
    }
}

// SC - O(N)
// TC -> O(N)

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */