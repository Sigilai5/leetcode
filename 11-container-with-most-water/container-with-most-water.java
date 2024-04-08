class Solution {
    public int maxArea(int[] height) {
        int i = 0;
        int j = height.length -1 ;

        int maximumCapacity = 0;

        while(i<j){
            int w = j - i;
            int h = Math.min(height[i],height[j]); 
            int capacity = w * h;
            maximumCapacity = Math.max(maximumCapacity,capacity);

            if(height[j] < height[i]){
                j-=1;
            }else{
                i+=1;
            }
        }

        return maximumCapacity;
        
    }
}

// SC -> O(1)
// TC -> O(N)