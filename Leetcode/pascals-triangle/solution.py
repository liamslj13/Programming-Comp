class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return[]
        if numRows == 1:
            return [[1]]
        prevRows = self.generate(numRows-1)
        row = [1] * numRows

        for i in range(1, numRows-1):
            row[i] = prevRows[-1][i-1]+prevRows[-1][i]

        prevRows.append(row)
        return prevRows

        
