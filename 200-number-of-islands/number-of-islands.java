class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;

        for(int i = 0; i < grid.length;i++){
            for(int j = 0;  j < grid[i].length;j++){
                if(grid[i][j] == '1'){ 
                    count+=sinkIsland(i,j,grid);
                }
            }
        }
        
        return count;
    }

    public int sinkIsland(int i , int j, char[][] grid){
        if(i < 0 || i >= grid.length || j < 0 || j >= grid[i].length || grid[i][j] == '0') return 0;

        grid[i][j] = '0';
        sinkIsland(i+1,j,grid);
        sinkIsland(i-1,j,grid);
        sinkIsland(i,j+1,grid);
        sinkIsland(i,j-1,grid);

        
        return 1;
    }
}

// SC -> O(1)
// TC -> O(N*M)