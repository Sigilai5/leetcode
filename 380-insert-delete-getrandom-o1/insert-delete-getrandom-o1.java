class RandomizedSet {

    HashSet<Integer> unique;

    public RandomizedSet() {
        unique = new HashSet();        
    }
    
    public boolean insert(int val) {
        if(unique.contains(val)) return false;

        unique.add(val);                
    
        return true;
    }
    
    public boolean remove(int val) {
        if(!unique.contains(val)) return false;

        unique.remove(val);

        return true;        
    }
    
    public int getRandom() {
        ArrayList<Integer> listItems = new ArrayList();

        for(Integer item: unique){
            listItems.add(item);
        }

        Random random = new Random();

        int randNumber = random.nextInt(listItems.size());

        return listItems.get(randNumber);
        
    }
}


// SC -> O(N)
// TC -> O(N)

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */