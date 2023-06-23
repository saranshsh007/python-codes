# A = [[1, 4, 5, 12], 
#     [-5, 8, 9, 0],
#     [-6, 7, 11, 19]]

# print("A =", A) 
# print("A[1] =", A[1])      # 2nd row
# print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
# print("A[0][-1] =", A[0][-1])   # Last element of 1st Row

# column = [];        # empty list
# for row in A:
#   column.append(row[2])   

# print("3rd column =", column)


# A = [[1,2,3] , [5,6,7] , [9,10,11]]
# B = [[1,2,3] , [5,6,7] , [9,10,11]]
# res = [[0,0,0] , [0,0,0] , [0,0,0]]

# for i in range (len(A)):
#     for j in range (len(B)):
#         res[i][j] = A[i][j]+B[i][j]


# for r in res:
#     print(r)

# # Transpose of a matrix

# A = [[1,2,3] , [5,6,7] , [9,10,11]]
# res = [[0,0,0] , [0,0,0] , [0,0,0]]

# for i in range (len(A)):
#     for j in range (len(res)):
#         res[j][i]=A[i][j]
# for r in res:
#     print(r)


# multiplication of two matrices :-

A = [[1,2,3] , [5,6,7] , [9,10,11]]
B = [[1,2,3] , [5,6,7] , [9,10,11]]
res = [[0,0,0] , [0,0,0] , [0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            res[i][j] += A[i][k]*B[k][j]

for r in res:
    print(r)