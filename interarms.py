nu1,nu2 = input().split()
nu1=int(nu1)
nu2=int(nu2)
nu1=nu1+1
st=[]
for i in range(nu1,nu2-1):
  power=len(str(i))
  temp=i
  sum=0
  while temp > 0:
    digit = temp % 10
    sum += digit ** power
    temp //= 10
  if i==sum:
    st.append(str(sum))
  else:
    continue
print(" ".join(st))
