class Solution {
    public int getKth(int lo, int hi, int k) {
        List<Integer> list = new ArrayList();           
        HashMap<Integer,Integer> map = new HashMap();
        
        for(int i = lo; i <= hi; i++){
            int x = i;
            int count = 1;
            while(x != 1){
                if(x%2 == 0){
                    x = x/2;
                    count++;
                }else{
                    x = (3*x) + 1;
                    count++;
                }
            }
            
            map.put(i,count);
            list.add(i);
        }
        
  
        Collections.sort(list,(a,b) ->  map.get(a) - map.get(b));
        
        
        List<Integer> output = list.subList(k-1,k);
        
        return output.get(0);
       
        
    }
}



