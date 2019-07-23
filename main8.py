n,x=input().split()
n=int(n)
x=int(x)
j=0
l=[]
sum=0
for i in range(n):
  no=int(input())
  l.append(no)
while(j<x):
  sum=sum+l[j]
  j+=1
print(sum)
