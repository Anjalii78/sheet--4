#you are provided with an integer array A return another array B of size same as that of A
# such that B[i]=A[i]^2
A = [2, 6, 8, 1]
B = []

for i in range(len(A)):
    B.append(A[i] ** 2)

print(B)
