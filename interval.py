x,y=input().split()
x=int(x)
y=int(y)
st=[]
for i in range(x,y):
  if(i%2!=0):
    st.append(str(i))
  else:
    continue
print(" ".join(st))
