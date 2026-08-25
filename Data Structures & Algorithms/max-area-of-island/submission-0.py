'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        So this basically is BFS on the islands where it is 1
        So I have to maintain a maximum area
    

        maxarea = 0

        def bfs(r,c):
            area = 0
            visited = set()

            if grid[r][c] == 1:
                area +=1

            directions = [[-1,0],[1,0],[0,1],[0,-1]]

            for dr,dc in directions:
                nr, nc = r+dr, c+dc

                if (nr < len(grid)) and (nc < len(grid[0])) and (grid[nr][nc] == 1):
                    bfs(nr,nc)
            
            return area

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = bfs(r,c)

                maxarea = max(maxarea,area)
        return maxarea
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        maxarea = 0
        visited = set()

        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return 0

            visited.add((r, c))

            area = 1

            directions = [
                [-1, 0],
                [1, 0],
                [0, -1],
                [0, 1]
            ]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                area += dfs(nr, nc)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs(r, c)
                    maxarea = max(maxarea, area)

        return maxarea