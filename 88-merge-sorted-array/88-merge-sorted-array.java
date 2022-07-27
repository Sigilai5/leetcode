class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if(m == 0 && n == 1){
            nums1[0] = nums2[0];
        }
        if(m == 1 && n == 0){
            nums1[0] =  nums1[0];
        }
        
        int nums1_counter = m;
        int nums2_counter = 0;
        while(nums1_counter < nums1.length && nums2_counter < nums2.length){
            nums1[nums1_counter] = nums2[nums2_counter];
            nums1_counter++;
            nums2_counter++;
        }
        
        Arrays.sort(nums1);
        
        System.out.print(Arrays.toString(nums1));
        
       
        
        
    }
}