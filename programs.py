#number related programs
#check a number is automorphic number or notot
#3/1/25
# 625-25*25=last 2 digits 25 76*76=1576-last two digit is the number squrw
num=int(input("enter a number:"))
len_num=len(str(num))
product=str(num*num)
res= "automorphic number " if (num==int(product[-len_num:]))else "mom"
print(res)

#one more method

num=int(input("enter a number:"))
len_num=len(str(num))
product=str(num*num)
res= "automorphic number " if (num==(num*num)%10**len_num) else "non-aut"
print(res)

##harshar number is if 3+7+8=18 and 378 is diviable by 18
#express sumof numbers can be expresd as the sum fo primw nunumbers
#74=71+3

num=int(input("enter a numbers:"))
comb=""
def prime(n):
  if n>1:
    for j in range(2,n//2+1):
      if n%j==0:
        return False
    return True
  return false
# print(prime(23))
# print(prime(36))
for i in range(2,num):
  if(prime(i) and prime(num-i)):
    comb=True
    break
if comb:
  print("true")
else:
  print("false")


##harshar number is if 3+7+8=18 and 378 is diviable by 18
#express sumof numbers can be expresd as the sum fo primw nunumbers
#74=71+3

# num=int(input("enter a numbers:"))
# comb=""
# def prime(n):
#   if n>1:
#     for j in range(2,n//2+1):
#       if n%j==0:
#         return False
#     return True
#   return false
# # print(prime(23))
# # print(prime(36))
# for i in range(2,num):
#   if(prime(i) and prime(num-i)):
#     comb=True
#     break
# if comb:
#   print("true")
# else:
#   print("false")
    


# #function basic

# def add (a,b):
#   return a+b
# print(add(20,30))
  
#4/1/25
lcm anf hcf of numbers in python

print("Hello, World!")
#lcm and gcd and hcf prpgrma
# lcm=a*b/gcd( a,b)
a=int(input("enter a number: "))
b=int(input("enter a number: "))
max_ab=a if (a>b) else b
temp=max_ab
while True:
  if max_ab%a==0 and max_ab%b==0:
   print("lcm is: ",max_ab)
   break
  max_ab+=temp
print("gcd",(a*b)/max_ab)
# this or this

print("Hello, World!")
#lcm and gcd and hcf prpgrma
# lcm=a*b/gcd( a,b)
a=int(input("enter a number: "))
b=int(input("enter a number: "))
for i in range(1,min(a,b)+1):
  if a%i==0 and b%i==0:
    gcd=i
print("gcd: " ,gcd)
print("lcm: ",(a%b)//gcd)

#6/1/25-next class-day
#problem solving statment with one example explanation

#fingidn the sum of inidivaal number sum in the one number which is there adn just inidival fibanxis number sum
num=input("enter a number:  ")
fibsum=0
def is_fib(n):
  a,b=0,1
  while True:
    if a==n:
     return True
    if a >n:
      return False
    a,b=b,a+b
    
for i in num:
  if(is_fib(int(i))):
    fibsum=fibsum+int(i)
print(fibsum)
 #7/1/25

      
    
  

