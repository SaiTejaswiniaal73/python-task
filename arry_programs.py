# 15/1/25
# code did not saved
# 16/1/25
# 1@finding the unique number in the list of arrays remaing the duplicates occurances
#remove dup in sorted arry of elements
# arr=[1,1,1,2,2,2,3,3,3,4,4,5,6,7,8,8,9,1,0]
# arr_uni=[]
# arr_dup
# for i in arr
num=input().split()
temp=[]
print(num)
for i in num:
  if i not in temp:
    temp.append(i)
print(temp)
i/p:
1 2  5 6 6 
o/p:
['1', '2', '5', '6', '6']
['1', '2', '5', '6']
#2 find the each rand for the each postin in the arr of elments

num=[int(i) for i in input().split()]
print(num)
temp=num.copy()
temp.sort()
print(temp)
res=""
for i in range(0,len(num)):
  for j in range (0,len(temp)):
    if num[i]==temp[j]:
      res=res+str(j+1)+" "
      break
print(res)
  i/p:
20 15 26 2 98 6
o/p:
[20, 15, 26, 2, 98, 6]
[2, 6, 15, 20, 26, 98]
4 3 5 1 6 2 

17/1/25
# 3 rearranign the arr in 1st half increaisng and 2nd half decrsing

num=[int(i) for i in input().split()]
print(num)
num.sort()
print(num)
mid=len(num)//2
print(mid)
first=num[0:mid]
secound=num[mid:]
print(first)
print(secound)
secound.sort(reverse=True)
print(secound)
print(* first+secound)#convert string to link with spcaes /w them

#i/p:8 7 1 6  5 9 0 4
#o/p:[8, 7, 1, 6, 5, 9, 0, 4]
[0, 1, 4, 5, 6, 7, 8, 9]
4
[0, 1, 4, 5]
[6, 7, 8, 9]
[9, 8, 7, 6]
0 1 4 5 9 8 7 6

# 4
#move all zeros to end and no negtive numbers to 1st


num=input().split(" ,")
nonzero=[]
print(num)
# num.sort()
for i in num:
  if i!="0":
    nonzero.append(i)

nonzero=nonzero+["0"]*(len(num)-len(nonzero))
print(nonzero)

print(" ,".join(nonzero))

#5 count max consecutives ones in the array
#i/p:{1,1,0,1,1,1}
#o/p:3


num=input().split(" ")
count=0
one_max=0
for i in num:
  if i=="1":
    count+=1
  else:
    count=0
one_max=max(one_max,count)
print(one_max)


#18/1/25
# 6 finde the number that come once in it
num=input().split()
temp=[]
x=False
count=0
print(num)
for i in num:
  if i not in temp:
    temp.append(i)
for i in temp:
  if num.count(i)==1:
    x=True
    break
if x:
  print(i)
else:
  print("no single term elemtn in the given array")
  #i/p : 1  2  3  2  3  4  1 7   7 and
# o/p:['1', '2', '3', '2', '3', '4', '1', '7', '7']
# 4

#using function


def repeated(num):
  temp=[]
  x=False
  for i in num:
    if i not in temp:
      temp.append(i)
  for i in temp:
    if num.count(i)==1:
      return i

  return "no single term elemtn in the given array"
num=input().split()
print(repeated(num))
#7 check if an arry of elemnst where 2 number sum is equal to target
def targetSum(num,target):
  for i in range (0,len(num)):
    for j in range(i+1,len(num)):
      if int(num[i])+int(num[j])==target:
        return "yes"
  return "no"
num=input().split()
target=140
print(targetSum(num,target))





















