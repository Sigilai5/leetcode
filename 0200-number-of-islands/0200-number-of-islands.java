class Solution {
    public int numIslands(char[][] grid) {
        if(grid.length == 0 || grid == null) return 0;  //Check for null values submitted
        
        int countIslands = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[i].length; j++){
                if(grid[i][j] == '1'){
                    countIslands += dfsCount(grid, i, j);                    
                }
                
            }
        }
        
        
        return countIslands;
        
    }
    
    public int dfsCount(char[][] grid, int i, int j){
        int islandFound  = 0;
        
        if(i < 0 || i >= grid.length || j < 0 || j >= grid[i].length){
            islandFound = 0;
        } else if(grid[i][j] == '0'){               
            islandFound = 0;
        } else if(grid[i][j] == '1'){
            grid[i][j] = '0';     //Sink island(Backtracking)
            dfsCount(grid,i+1,j); // Dow
            dfsCount(grid,i-1,j); // Up
            dfsCount(grid,i,j+1); // Right
            dfsCount(grid,i,j-1); // Left
            islandFound = 1;
            
        } else{
            islandFound = 0;
        }
        
        return islandFound;
        
    }
    
}