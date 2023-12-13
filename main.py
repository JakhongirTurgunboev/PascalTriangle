from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        triangle = [[1]]
        current = [1]
        for _ in range(rowIndex):
            prev = triangle[-1]
            current = [1]
            for i in range(1, len(prev)):
                current.append(prev[i - 1] + prev[i])
            current.append(1)
            triangle.append(current)

        return current