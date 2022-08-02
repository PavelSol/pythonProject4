import copy
n = int(input())
mat = []
c = 1
for i in range(0, n):
    b = []
    for j in range(0, n):
        b.append(c)
        c += 1
    mat.append(b)
mat2 = [[0]*n]*n
print(mat2)
mat2[0] = mat[0]
print(mat2)


