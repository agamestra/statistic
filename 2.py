A=[]
A=input().split()
for i in range(len(A)):
    A[i]=int(A[i])
t=int(input())
b=int(len(A))
for i in range (t):
    c=A[b-1]
    d=b-A[b-1]-1
    A.pop()
    A.insert(d,c)
print(A)