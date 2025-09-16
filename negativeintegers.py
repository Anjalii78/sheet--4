
#Write a program to print all negative number from input array A or size N

A = list(map(int, input().split()))  
for num in A:
    if num < 0:
        print(num)
