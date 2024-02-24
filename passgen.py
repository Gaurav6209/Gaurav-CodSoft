import random
l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
l2 =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
l3 = ['1','2','3','4','5','6','7','8','9','0']
l4 = ['!','@','#','$','%','^','&','*','(',')','_','-','=','+']
l5 = l1+l2+l3+l4
a = int(input("Enter the length of your password: "))
if (a<8):
  print("Password must be at least 8 characters long")
else:
  random.shuffle(l5)
  for i in range(0,a):
    print(l5[i], end="")
  
    
    