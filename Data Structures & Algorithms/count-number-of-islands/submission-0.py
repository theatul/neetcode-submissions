class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 # is this correct?

        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for i in range(cols)] for j in range(rows)]
        islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0" or visited[i][j]== True:
                    continue
                
                # start a new island and do BFS
                queue = []
                queue.append([i,j])
                while queue:
                    temp = queue.pop(0)
                    l = temp[0]
                    k = temp[1]
                    # Add all adjacent connected lands to queue
                    if self.isValid(l-1,k,rows,cols) and grid[l-1][k] == "1" and visited[l-1][k] != True:
                         queue.append([l-1,k])
                    if self.isValid(l+1,k,rows,cols) and grid[l+1][k] == "1" and visited[l+1][k] != True:
                         queue.append([l+1,k])
                    if self.isValid(l,k-1,rows,cols) and grid[l][k-1] == "1" and visited[l][k-1]!= True:
                         queue.append([l,k-1])
                    if self.isValid(l,k+1,rows,cols) and grid[l][k+1] == "1" and visited[l][k+1]!= True :
                         queue.append([l,k+1])
                    visited[l][k] = True
                islands += 1

        return islands
    
    def isValid(self, l,k,rows,cols):
        if l >= 0 and l < rows and k>=0 and k<cols:
            return True
        return False 


        