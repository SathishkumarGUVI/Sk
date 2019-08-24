lower,upper =input().split()
lower=int(lower)
upper=int(upper)
upper=upper+1
st=[]
for num in range(lower,upper-1):
      if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           st.append(str(num))
print(" ".join(st))
