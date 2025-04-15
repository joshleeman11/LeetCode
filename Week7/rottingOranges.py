from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def runRottingProcess(minutes):
            continueRotting = False
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == minutes:
                        for d in directions:
                            new_row, new_col = row + d[0], col + d[1]

                            if rows > new_row >= 0 and cols > new_col >= 0:
                                if grid[new_row][new_col] == 1:
                                    grid[new_row][new_col] = minutes + 1
                                    continueRotting = True
            return continueRotting

        minutes = 2
        while runRottingProcess(minutes):
            minutes += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return minutes - 2