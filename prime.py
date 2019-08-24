numb = int(input())
if numb > 1:
   for i in range(2, numb//2): 
       if (numb % i) == 0: 
           print("no") 
           break
   else: 
        print("yes") 

else: 
   print("no")
