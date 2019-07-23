string=input()
k=0
l=0
v=['a','e','i','o','u']
c=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
for j in range(21):
  if(c[j]==string):
     print("Consonant")
     break
  else:
     k+=1
for i in range(5):
  if(v[i]==string):
     print("Vowel")
     break
  else:
     l+=1
if(k==21 and l==5):
  print("invalid")
