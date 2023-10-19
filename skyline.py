class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Take max of each row.
        row = [0]*len(grid)
        col = []
        answer = 0
        for i in range(0,len(grid)):
            row[i] = max(grid[i])
        for j in range(0,len(grid)):
            c = []
            for k in range(0,len(grid)):
                c.append(grid[k][j])
            col.append(max(c))
        for ans in range(0,len(grid)):
            for sol in range(0,len(grid)):
                answer += min(row[ans],col[sol]) - grid[ans][sol] 
        return answer
        
            
