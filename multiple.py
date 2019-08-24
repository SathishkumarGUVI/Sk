n=int(input())
a=n
i=1
st=[]
while(i<6):
  n=n*i
  st.append(str(n))
  n=a
  i=i+1
print(" ".join(st))
