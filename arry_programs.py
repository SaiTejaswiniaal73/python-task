# 15/1/25
# code did not saved
# 16/1/25
# @finding the unique number in the list of arrays remaing the duplicates occurances
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
#find the each rand for the each postin in the arr of elments

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
