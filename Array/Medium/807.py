"""
Number: 807
Title: Max Increase to Keep City Skyline
Difficulty: Medium
Date: 01-24-2023
Link: https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
"""

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        rowMax = [0] * n
        colMax = [0] * n
        for r in range(n):
            for c in range(n):
                rowMax[r] = max(grid[r][c], rowMax[r])
                colMax[c] = max(grid[r][c], colMax[c])
        
        sum = 0
        for r in range(n):
            for c in range(n):
                newHeight = min(rowMax[r], colMax[c])
                sum += newHeight - grid[r][c]
                grid[r][c] = newHeight

        return sum