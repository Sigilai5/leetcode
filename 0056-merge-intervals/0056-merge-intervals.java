class Solution {
    public int[][] merge(int[][] intervals) {
        if(intervals.length <= 1) return intervals;  //check for null and one array input as well
        //[[1,3],[8,10],[15,18],[2,6]]
        
        Arrays.sort(intervals,(arr1,arr2) -> Integer.compare(arr1[0],arr2[0])); //sort by first element
        //[[1,3],[2,6],[8,10],[15,18]]
        
        List<int[]> outputArray = new ArrayList(); //create a list(it offers flexibility)
        
        outputArray.add(intervals[0]); // [[1,3]]
        
        int current = 0; //Pointer to current interval
        int next = 1; // Pointer to next interval
        
        while(next < intervals.length){
            int[] currentInterval = outputArray.get(current); // [1,3]
            int[] nextInterval = intervals[next]; // [2,6]
            
            if(nextInterval[0] <= currentInterval[1]){  // check if 2 in [2,6] is less than 3 in [1,3], if so there is an overlap 
              currentInterval[1] = Math.max(currentInterval[1],nextInterval[1]);    // Replace the 3 in [1,3] with 6 in [2,6] 
            }else{
                outputArray.add(nextInterval); //there is no overlap,so add the nextInterval to our outputArray
                current++; //move current pointer to next interval
            }
            
            next++; //move next pointer to the next interval
        }
        
        
        
        return outputArray.toArray(new int[outputArray.size()][]);  //covert list to 2D array
        
        
    }
}