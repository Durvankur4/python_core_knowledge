# Quesiton:

# Rotting Fruit
# Medium
# Topics
# Company Tags
# Hints
# You are given a 2-D matrix grid. Each cell can have one of three possible values:

# 0 representing an empty cell
# 1 representing a fresh fruit
# 2 representing a rotten fruit
# Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

# Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

# Example 1:
# Solution:
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()
        fresh = 0
        time = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        
        
        neighbours = [[0,1],[1,0],[0,-1],[-1,0]]
        while queue and fresh > 0 :
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for n,m in neighbours:
                    n_r = r + n
                    n_c = c + m

                    if n_r >= ROW or n_c >= COL or n_r < 0 or n_c < 0 or grid[n_r][n_c]!=1:
                        continue 
                    
                    if grid[n_r][n_c]==1:
                        grid[n_r][n_c] = 2
                        queue.append((n_r,n_c))
                        fresh -= 1

            time += 1
        return time if fresh == 0 else -1



         

# time complexity = O(n)
# space complexity = O(n)
