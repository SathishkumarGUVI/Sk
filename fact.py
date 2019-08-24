nu = int(input())
factorial = 1
if nu == 0:
   print(1)
else:
   for i in range(1,nu + 1):
       factorial = factorial*i
   print(factorial)
