# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 250

#@profile
def multiplyMatrices_opt():

    # NxN matrix
    X = np.random.rand(N, N)
    # Nx(N+1) matrix
    Y = np.random.rand(N, N+1)
    
    result = np.matmul(X,Y)
        
    print(result)

multiplyMatrices_opt()


# #X=[]
# 	X = np.array([])
# 	for i in range(N):
#     		X.append([random.randint(0,100) for r in range(N)])


# #Y=[]
# 	Y = np.array([])
# 	for i in range(N):
#     		Y.append([random.randint(0,100) for r in range(N+1)])

# # result is Nx(N+1)
# 	result = []
# 	for i in range(N):
#     		result.append([0] * (N+1))


# # iterate through rows of X
# 	for i in range(len(X)):
# # iterate through columns of Y
#     		for j in range(len(Y[0])):
#         # iterate through rows of Y
#         		for k in range(len(Y)):
#             			result[i][j] += X[i][k] * Y[k][j]

# #line 30 and 31 should be optimzed, matrix optimization
# return result

# # for r in result:
# #     print(r)

