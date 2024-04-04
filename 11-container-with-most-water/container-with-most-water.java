class Solution {
    public int maxArea(int[] height) {
        int i = 0;
        int j = height.length - 1;

        int mostWater = 0;

        while(i < j){
            int w = j - i;
            int h = Math.min(height[i],height[j]);

            int capacity = w * h;

            mostWater = Math.max(capacity,mostWater);

            if(height[i] < height[j]){
                i+=1;
            }else{
                j-=1;
            }

        }

        return mostWater;
        
    }
}

// SC -> O(1)
// TC -> O(N)