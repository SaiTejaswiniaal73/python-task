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
  if a%i==0 and b%i==0:s
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
#if if give input any numbe rand we need to get nearest fib number


#neart fin number for the input
number=76
a=0
b=1
i=1
while(a<=number):
  # print(a)
  c=a+b
  a=b
  b=c
  # i=i+1
# print(a,b-a)
#a is right b-a is left
print(a,b-a)
if(number-(b-a)<a-number):
  print(b-a,"neart number")

else:
  print(a,"near num")

#print fib is the number is fib
#neart fin number for the input
number=34
a=0
b=1
i=1
while(a<=number):
  # print(a)
  c=a+b
  a=b
  b=c
  # i=i+1

#a is right b-a is left
print(a,b-a)
if((b-a)==number):
  print(b-a,"it is fib")
elif((number-(b-a))<a-number):
  print(b-a,"neart number")
else:
  print(a,"near num")
  
  
 #find the highest prime number if the given number digits

#prime number in given digits
num="12345689"
res=" "
first=1
def is_prime(n):
  if n>1:
    for i in range(2,(n//2)+1):
      if n%i==0:
        return False
    return True
  return False
# print(is_prime(174))
for digit in num:
  if (is_prime(int(digit))):
    # res+=digit
# print(res)
    if(first==1):
      maxprime=digit
      first=first+1
    else:
      if digit>maxprime:
        maxprime=digit
print(maxprime)
    

    
#  max prime withput function

#exprerss anuber number with sum of 2 primes
#i/p:18,o/p:17 19
#i/p:20 o/p:19,23
num=18
def is_prime(n):
  if(n>1):
    for i in range(2,((n//2))+1):
      if n%i==0:
        return False
    return  True
  return False
if(is_prime(num)):
  print("it is prime")
else:
  lp,rp=num-1,num+1
  
  while True :
    if (is_prime(lp)):
      print(lp)
      break
    lp-=1
  while True :
    if (is_prime(rp)):
      print(rp)
      break
    rp+=1


#or


num=int(input("enter num:"))
def prime(n):
  if n>1:
    for i in range(2,(n//2)+1):
      if n%i==0:
        return False
      return True
    return False

if(prime(num)):
  print("it is prime")
else:
  left,right=num-1,num+1
  while True:
    if(prime(left)):
      break
    left-=1
    
  while True:
      if(prime(right)):
        break
      righ+=1
  print(left,right)
  res="{} {}".format(left,right)if(num-left==right-num) else left if(num-left<right-num) else right
  print(res)
  
#i/p=187
write the sum of max and min prime of given number=8765432
o/p=5+7
o/p=12
num="134572689"
res=" "
first=1
firstt=1
def is_prime(n):
  if n>1:
    for i in range(2,(n//2)+1):
      if n%i==0:
        return False
    return True
  return False
# print(is_prime(174))
for digit in num:
  if (is_prime(int(digit))):
    # res+=digit
# print(res)
    if(first==1):
      maxprime=digit
      first=first+1
    else:
      if digit>maxprime:
        maxprime=digit
print(maxprime)
for digit in num:
  if (is_prime(int(digit))):
    # res+=digit
# print(res)
    if(firstt==1):
      minprime=digit
      firstt=firstt+1
    else:
      if digit<minprime:
        minprime=digit
print(minprime)
res=int(maxprime)+int(minprime)
print(res)

#8/1/25

#fib numbers
num=int(input("enter num:"))
a,b,non_fib=0,1,0
while non_fib!=num:
  for i in range(a+1,b):
    non_fib +=1
    print(i,end=" , ")
    if non_fib==num:
      break
  a,b=b,a+b

#binaru to num
num=int(input(""))
count=0
temp=num
dec=0
while num!=0:
  rem=num%10
  dec=dec+(2**count)*rem
  num=num//10
  count+=1
print("decimal for {} is {}".format(temp,dec))
  
  
#if i/p is string bin to decimal
num=input("enter a num: ")
dec=0
for i in range (len(num)-1,-1,-1):
  dec+=(2**(len(num)-i-1))*int(num[i])
print(dec)
#homw work
#program to convet decimal to binaru
i/p:5 o/p:101
#prints sum of non_fib numbers as per the i/p
i/p:3
o/p:17


#9/1/25
#program to convet decimal to binaru
#decimal to binary
num=int(input("entera num:"))
s=" "
while (num!=0):
  rem=num%2
  s=str(rem)+s
  num=num//2
print(s)
#aramstrong numbers

  #retrun if arm strong
# 1cube+3 cube+5 cube=153//sum of powers of inidvial digits is called as aramstog

num=input("enter a num: ")
res=0
power=len(num)
for i in num:
  res+=int(i)**power
print(num==str(res))
print(res,num)
#list of number tell the number
num1=int(input("enter a num: "))
def armstrong(num):
  res=0
  power=len(num)
  for i in num:
    res+=int(i)**power
  return num==str(res)
for i in range(1,num1+1):
  if(armstrong(str(i))):
    print(i)

#check wheather a num is perfect umber or not

# factprs of 15-1,5,3-not perfcat
# fact of 6-1,2,3--perfect
# fact of 28-1,2,4,7,14--perfect
#perfect number are not
# factore of 15 -- 1,3,5
num=int(input("enter a num: "))
sum=0
for i in range(1,num//2+1):
  if num%i==0:
    sum+=i
if (sum==num):
  print(f"{num} is a perfect num")
else:
  print(f"{num}is  not a perfect num")
  
#o/p
#enter a num: 27is  not a perfect num
#enter a num: 28 is a perfect num




#10/1/25

#i/p:abcdcd
# o/p:
# 2-cdc - it is 2 times in the main string

string1="abcdcdc"
sub_string="cdc"
count=0
for i in range(0,len(string1)):
  if string1[i]==sub_string[0]:
    if(string1[i:i+len(sub_string)]==sub_string):
      count+=1
print(count)


#range of perfect number
num=int(input("enter a num to find perfect numbe range:"))
count=0
for j in range(1,num+1):
  res=0
  for i in range(1,(j//2)+1):
    if j%i==0:
      res=res+i
      # print(res)
  if(j==res):
    print(j)
    count+=1
print(count)
    
i/p:1000
o/p:6,28,496

#rev numbers:

num=int(input("enter a num to find reverse numbe range:"))
temp,res=num,0
while num!=0:
  rem=num%10
  res=res*10+rem
  # res=res+num
  # res+=1
  num=num//10
print(res==temp)
print(res)
  
#15/1/25










































    

  
























































  
  
 



      
    
  

