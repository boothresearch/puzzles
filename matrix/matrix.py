class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        print (self[index])
            

    def column(self, index):
        pass    
            
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]

mat_test = Matrix(matrix)
mat_test.row(index=1)
