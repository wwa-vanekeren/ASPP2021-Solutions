# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:15:18 2021

@author: wesva399
"""
import numpy as np
print("Create a null vector of size 10")
a=np.zeros(10)
print(a)
print("Update fifth value of vector a with 1")
a[4]=1
print(a)

print("Show numpy vector y with values 10-49")
b=np.arange(10,49)
print(b)

print("Reverse order of vector b")
c=b[::-1]
print(c)

print("Create 3x3 matrix with values ranging from 0 to 8")
d=np.arange(0,9).reshape(3,3)
print(d)

print("Find indices of non-zero elements from [1,2,0,0,4,0]")
e=np.array([1,2,0,0,4,0])
print(e)
f=np.nonzero(e)
print(f)

print("Create a random vector of size 30 and find the mean value")
g=np.random.rand(30)
print(g)
h=np.mean(g)
print(h)

print("Create a 2d array with 1 on the border and 0 inside")
i=np.ones((3,3))
print("2d array")
print(i)
print("0 inside")
i[1,1]=0
print(i)

print("Create a 8x8 matrix and fill it with a checkerboard pattern")
h1 = np.ones(8)
h1[::2] = 0
h2 = h1[::-1]
h = np.array([h1,h2,h1,h2,h1,h2,h1,h2])
print(h)

print("Create a checkerboard 8x8 matrix using the tile function")
j = np.array([[0,1],[1,0]])
j = np.tile(j,(4,4))
print(j)

print("Given a 1D array, negate all elements which are between 3 and 8, in place")
k = np.arange(11)
jdxk = np.where((k<=8)&(k>=3))
k[jdxk] *= -1
print(k)

print("Create a random vector of size 10 and sort it")
l = np.random.random(10)
l[:] = np.sort(l)
print(l)

print("Consider two random array A anb B, check if they are equal")
A = np.random.rand(1,1,1)
B = np.random.rand(1,1,1)
Equal = A == B
print(Equal)

print("How to convert an integer (32 bits) array into a float (32 bits) in place?")
m = np.arange(10, dtype=np.int32)
print(m.dtype)
m.dtype = np.float32
print(m.dtype)

print("How to get the diagonal of a dot product?")
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)
print(D)

