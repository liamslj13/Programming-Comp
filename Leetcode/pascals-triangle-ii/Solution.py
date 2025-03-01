class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        prevRow = self.getRow(rowIndex - 1)
        row = [1] * len(prevRow)

        for i in range(1, len(row)):
            row[i] = prevRow[i] + prevRow[i-1]

        row.append(1)
        return row

        
