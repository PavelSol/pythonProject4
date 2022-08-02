n = int(input())
mat = []
c = 1
for i in range(0, n):
    b = []
    for j in range(0, n):
        b.append(c)
        c += 1
    mat.append(b)
for i in range(0, n):
    print(*mat[i])