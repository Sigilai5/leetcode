class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if(image.length == 0 || image == null) return image;
        if(image[sr][sc] == color) return image;
        
        for(int i = 0; i < image.length;i++){
            for(int j = 0; j < image[i].length;j++){
                
                if(i == sr && j == sc){
                    int startingPixel = image[i][j];
                    dfs(image,i,j,color,startingPixel);
                }
        }
        
    }
        
   return image;     
        
}
    
    public void dfs(int[][] image, int i, int j, int color,int startingPixel){
        if(i < 0 || j < 0 || i >= image.length || j >= image[i].length || image[i][j] != startingPixel){
            return;
        }
        
        image[i][j] = color;
        dfs(image,i-1,j,color,startingPixel); // Up 
        dfs(image,i+1,j,color,startingPixel); // Down
        dfs(image,i,j-1,color,startingPixel); // Left
        dfs(image,i,j+1,color,startingPixel); // Right
        
    }
    
    
    
    
}