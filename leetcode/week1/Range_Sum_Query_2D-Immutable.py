#Time Complexity O(1)

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.offset = 1
        #https://peps.python.org/pep-0008/#constants
        ROWS, COLS = len(matrix), len(matrix[0])
        #initialize sumMatrix with 0's and extra row, col pad for easier calulcation of sums after init
        #https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        self.sumMatrix = [[0 for col in range(COLS + self.offset)] for row in range(ROWS + self.offset)]

        print (self.sumMatrix)
        
        for row in range(ROWS):
            prefix = 0
            for col in range(COLS):
                prefix += matrix[row][col]
                print(row, col)
                self.sumMatrix[row+1][col+1] = prefix + self.sumMatrix[row][col+1] 
 
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        r1, c1, r2, c2 = row1+self.offset, col1+self.offset, row2+self.offset, col2+self.offset
        return self.sumMatrix[r2][c2] - self.sumMatrix[r1-1][c2] - self.sumMatrix[r2][c1-1] + self.sumMatrix[r1-1][c1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
