class RandomizedSet {
    Map<Integer,Integer> valIndex;
    List<Integer> vals;
    Random random;

    public RandomizedSet() {
        valIndex = new HashMap<>();
        vals = new ArrayList<>();
        random = new Random();
    }
    
    public boolean insert(int val) {
        if(valIndex.containsKey(val)) return false;

        valIndex.put(val,vals.size());
        vals.add(val);

        return true;
        
    }
    
    public boolean remove(int val) {
        if(!valIndex.containsKey(val)) return false;

        int lastVal = vals.get(vals.size() - 1);
        int idx = valIndex.get(val);

        vals.set(idx,lastVal);
        valIndex.put(lastVal,idx);


        vals.remove(vals.size() - 1);
        valIndex.remove(val);

        return true;
        
    }
    
    public int getRandom() {
        return vals.get(random.nextInt(vals.size()));        
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