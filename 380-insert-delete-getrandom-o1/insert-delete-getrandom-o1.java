class RandomizedSet {
    HashMap<Integer,Integer> valIndex;
    ArrayList<Integer> vals;

    public RandomizedSet() {
        valIndex = new HashMap();
        vals = new ArrayList();
    }
    
    public boolean insert(int val) {
        if(valIndex.containsKey(val)) return false;
        valIndex.put(val,vals.size());
        vals.add(val);

        return true;
    }
    
    public boolean remove(int val) {
        if(!valIndex.containsKey(val)) return false;

        int getLastItem = vals.get(vals.size() - 1);
        int getKey = valIndex.get(val);

        // Delete from dictionary
        valIndex.put(getLastItem,getKey);
        valIndex.remove(val);

        // delete from list
        vals.set(getKey, getLastItem);
        vals.remove(vals.size() - 1);

        return true;
        
    }
    
    public int getRandom() {
        Random random = new Random();

        return vals.get(random.nextInt(vals.size()));
        
    }
}

// SC => O(N)
// TC -> O(1)

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */