import random


def RPS():
  list1 = ['a','b','c']
  a = 'stone'
  b = 'paper'
  c = 'scissors'
  q = input("Enter a for stone \n Enter b for papaer \n Enter c for scissors"+ ':')
  r = random.choice(list1)
  if(q==r):
     print("you choose"+ " " + q)
     print("computer choose"+ " " + r)
     print("It is a draw")
     print("You gained 0 point")
  elif(q=='a' and r=='b' or q=='b' and r=='c' or q=='c' and r=='a'):
     print("you choose"+ " " + q)
     print("computer choose"+ " " + r)
     print("You loose")
     print("You gained 0 point")
  elif(q=='a' and r=='c' or q=='b' and r=='a' or q=='c' and r=='a' ):
     print("you choose"+ " " + q)
     print("computer choose"+ " " + r)
     print("You Win")
     print("You gained 1 point")
  
while(True):
  RPS()
  n = int(input("Enter 1 to play again and 0 to exit: "))
  if(n==0):
    break

   

