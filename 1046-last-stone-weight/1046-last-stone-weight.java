class Solution {
    public int lastStoneWeight(int[] stones) {
        if(stones.length == 1) return stones[0];
        
        PriorityQueue<Integer> bigToSmall = new PriorityQueue();
        for(int stone:stones){
            bigToSmall.add(-stone);
        }
        
        while(bigToSmall.size() > 1){
            int bigStone = -bigToSmall.poll();
            int smallStone = -bigToSmall.poll();
            
            if(bigStone != smallStone){
                bigToSmall.add(-(bigStone - smallStone));
            } 
        }
                           
        if(bigToSmall.isEmpty()){
            return 0;
        } 
        
        return -bigToSmall.poll();
                           
        
        
    }
}