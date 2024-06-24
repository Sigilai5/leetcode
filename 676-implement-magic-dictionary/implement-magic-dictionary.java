class MagicDictionary {
    List<String> dict;
    
    public MagicDictionary() {
        dict = new ArrayList();
    }
    
    public void buildDict(String[] dictionary) {
        for(String st: dictionary){
            dict.add(st);
        }
        
    }
    
    public boolean search(String searchWord) {
        for(int i = 0; i < dict.size();i++){
            if(dict.get(i).length()== searchWord.length()){
                String check = dict.get(i);
                int count = 0;
                for(int j = 0; j < searchWord.length();j++){
                    if(searchWord.charAt(j) != check.charAt(j)){ 
                        count+=1;
                    }
                }
                if(count == 1) return true;
            }
        }

        return false;
                
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dictionary);
 * boolean param_2 = obj.search(searchWord);
 */