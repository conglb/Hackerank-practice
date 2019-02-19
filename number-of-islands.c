char **arr;
int r,c;
int numIslands(char** grid, int gridRowSize, int gridColSize) {
    arr = grid;
    r = gridRowSize;
    c = gridColSize;
    for (int i=0; i<gridRowSize; i++) {
        for (int j=0; j<gridColSize; j++) {
            if (grid[i][j] == '1') {
                dfs(i,j);
            }
        }
    }
}

void dfs(int x, int y) {
    if (x < 0 || x >= r || y < 0 || y >= c) {
        return
    }
    arr[x][y] = 0;
    dfs(x+1, y);
    dfs(x, y+1);
    dfs(x, y-1);
    dfs[x-1, y];
}