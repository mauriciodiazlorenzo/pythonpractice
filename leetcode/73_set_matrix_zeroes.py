# time: O(n*m)
# space: O(n+m)
matrix = [[1,1,1],[1,0,1],[1,1,1]]
rows_to_zero=[]
columns_to_zero=[]
for ind_i, i in enumerate(matrix):
    for ind_j, j in enumerate(i):
        if j == 0:
            rows_to_zero.append(ind_i)
            columns_to_zero.append(ind_j)
for ind_i in rows_to_zero:
    for ind_j in range(0,len(matrix[ind_i])):
        matrix[ind_i][ind_j]=0
for ind_i in range(0,len(matrix)):
    for ind_j in columns_to_zero:
        matrix[ind_i][ind_j]=0

# use the first elements of each column and row to indicate if that column or row should be zeroed
# EXCEPT for the first row and column, which share the topleft bit, so these must be stored separately as variables
# time: O(m*n)
# space: O(1)
matrix = [[1,1,1],[1,0,1],[1,1,1]]
row1zero=False
col1zero=False
for j in matrix[0]:
    if j==0:
        row1zero=True
for i in matrix:
    if i[0]==0:
        col1zero=True
for i in range(1,len(matrix)):
    for j in range(1,len(matrix[0])):
        if matrix[i][j]==0:
            matrix[i][0]=0
            matrix[0][j]=0
print(matrix)
for i in range(1,len(matrix)):
    for j in range(1,len(matrix[0])):
        if matrix[0][j]==0 or matrix[i][0]==0:
            matrix[i][j]=0
if row1zero:
    for j in range(0, len(matrix[0])):
        matrix[0][j]=0
if col1zero:
    for i in range(0, len(matrix)):
        matrix[i][0]=0
print(matrix)

