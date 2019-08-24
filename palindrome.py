number=int(input())
tem=number
re=0
while(number>0):
    dig=number%10
    re=re*10+dig
    number=number//10
if(tem==re):
    print("yes")
else:
    print("no")

