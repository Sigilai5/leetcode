class Solution {
    public int maxArea(int[] height) {
        int mostWater = 0;
        int i = 0;
        int j = height.length -1;

        while(i < j){
            int l = j - i;
            int h = Math.min(height[i],height[j]);

            mostWater = Math.max(mostWater, h*l);

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