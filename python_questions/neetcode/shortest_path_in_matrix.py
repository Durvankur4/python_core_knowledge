# Quesiton:

# Shortest Path in Binary Matrix
# Medium
# Topics
# Company Tags
# You are given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.
# Solution:

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COl = len(grid[0])
        queue = deque()
        visited = set()

        if grid[0][0] == 1 or grid[ROW-1][COl-1]== 1:
            return -1

        queue.append((0,0))
        visited.add((0,0))
        length = 1

        

        while(queue):
            

            for i in range(len(queue)):
                r,c = queue.popleft()
                print((r,c))
                if r == ROW-1 and c == COl-1:
                    return length

                neighbours = [
    (-1,-1), (-1,0), (-1,1),
    (0,-1),          (0,1),
    (1,-1),  (1,0),  (1,1)
]
                for n,m in neighbours:
                    n_r = r+n
                    n_c = c+m
                    if n_r<0 or n_c<0 or n_r>= ROW or n_c>=COl or ((n_r,n_c) in visited) or grid[n_r][n_c] == 1:
                        continue
                    print(n_r,n_c)
                    queue.append((n_r,n_c))
                    visited.add((n_r,n_c))

            length += 1

        return -1
# time complexity = O(n)
# space complexity = O(n)
