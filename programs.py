#number related programs
#check a number is automorphic number or notot

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
    
