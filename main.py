n, m = map(int,input("Enter the two numbers you want to perform operations: ").split())
sum = n+m
sub = n-m
mult = n*m
div = n/m
modu = n%m
expo = n**m
floor = n//m
a = int(input("Enter 1 for addition\n      2 for subtraction\n      3 for multiplication\n      4 for division\n      5 for modulus\n      6 for exponential\n      7 for floor division: "))
if a==1:
  print("The sum is : ", sum)
if a==2:
  print("The subtraction is : ", sub)
if a==3:
  print("The multiplication is : ", mult)
if a==4:
  print("The division is : ", div)
if a==5:
  print("The modulus is : ", modu)
if a==6:
  print("The exponential is : ", expo)
if a==7:
  print("The floor division is : ", floor)
  