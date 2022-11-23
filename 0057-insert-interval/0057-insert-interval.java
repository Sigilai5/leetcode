class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
              
        int[][] newArr = new int[intervals.length+1][2];
        int pointer = 0;
        for(int[] interval: intervals){
            newArr[pointer] = interval;
            pointer++;
        }
        newArr[newArr.length -1] = newInterval;
        
        Arrays.sort(newArr, (arr1,arr2) -> Integer.compare(arr1[0],arr2[0]));
        
        List<int[]> output = new ArrayList();
        
        output.add(newArr[0]);
        
        int current = 0;
        int next = 1;
        
        while(next < newArr.length){
            int[] currentInterval = output.get(current);
            int[] nextInterval = newArr[next];
            
            if(nextInterval[0] <= currentInterval[1]){
                currentInterval[1] = Math.max(currentInterval[1],nextInterval[1]);
            }else{
                output.add(nextInterval);
                current++;
            }
            
            next++;
        }
        
        
        
        
        return output.toArray(new int[output.size()][]);
    }
}