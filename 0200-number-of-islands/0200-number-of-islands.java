class Solution {
    public int numIslands(char[][] grid) {
        if(grid.length == 0 || grid == null) return 0;
        int countIsland = 0;
        
        for(int i = 0;i < grid.length;i++){
            for(int j = 0; j < grid[i].length;j++){
                if(grid[i][j] == '1'){
                    countIsland += sinkIsland(grid,i,j);  //Sink Island
                    
                }
                
            }
        }
        
      return countIsland;
        
    }
    
    
    public int sinkIsland(char[][] grid, int i, int j){
        int count = 0;
        
        if(i < 0 || i >= grid.length || j < 0 || j >= grid[i].length){
            count = 0;
        }else if(grid[i][j] == '0'){
            count = 0;
        }else if(grid[i][j] == '1'){
            grid[i][j] = '0';
            sinkIsland(grid,i-1,j); //Sink Left
            sinkIsland(grid,i,j-1); //Sink top
            sinkIsland(grid,i,j+1); //Sink Bottom
            sinkIsland(grid,i+1,j); //Sink right
            count = 1;
        }else{
            count = 0;
        }
        
            
        
        return count;
        
    }
    
}

//Time Complexity -> O(n*m)
//Space Complexity -> O(1)