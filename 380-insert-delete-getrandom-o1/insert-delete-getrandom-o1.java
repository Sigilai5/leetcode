class RandomizedSet {
    Map<Integer,Integer> val_index;
    List<Integer> vals;
    Random random;

    public RandomizedSet() {
        this.val_index = new HashMap<>();
        this.vals = new ArrayList<>();
        this.random = new Random();
    }
    
    public boolean insert(int val) {
        if(this.val_index.containsKey(val)) return false;

        this.val_index.put(val,this.vals.size());
        this.vals.add(val);

        return true;
    }
    
    public boolean remove(int val) {
        if(!this.val_index.containsKey(val)) return false;

        // get last val
        int lastVal = this.vals.get(this.vals.size()  - 1);
        // get index of val
        int idx = this.val_index.get(val);

        // replace list
        this.vals.set(idx,lastVal);
         // replace map
        this.val_index.put(lastVal,idx);
               
        // delete from list
        this.vals.remove(this.vals.size() - 1);
        // delete from map
        this.val_index.remove(val);

        return true;
    }
    
    public int getRandom() {
        int randIndex = this.random.nextInt(0, this.vals.size()); 
        return this.vals.get(randIndex);        
    }
}

// SC -> O(N)
// TC -> O(1)

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */