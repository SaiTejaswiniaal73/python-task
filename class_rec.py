#tuples class missing
#set continution 31/12/24
set in python set can add,create,del;te elemts
write ste defitnation 
in sets indexing not possiable
s1={2,3,4,"true","hello","true",}

set:set is a collectionof elemnts ,spreated by commac wirj

s1={1,2,3,"true","hi","a"}
for i in s1:
  print(s1)


Python Sets
A set is a collection of unique data, meaning that elements within a set cannot be duplicated.
In Python, we create sets by placing all the elements inside curly braces {}, separated by commas.

A set can have any number of items and they may be of different types (integer, float, tuple, string, etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements.
# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

Let's see what will happen if we try to include duplicate items in a set.

numbers = {2, 4, 6, 6, 2, 8}
print(numbers)   # {8, 2, 4, 6}



#add and update
#add
# In Python, we use the add() method to add an item to a set. For example,
numbers = {21, 34, 54, 12}
print('Initial Set:',numbers)

# using add() method
numbers.add(32)
print('Updated Set:', numbers) 

# Output
# Initial Set: {34, 12, 21, 54}
# Updated Set: {32, 34, 12, 21, 54}

#update

# The update() method is used to update the set with items other collection types (lists, tuples, sets, etc). For example,

companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

# using update() method
companies.update(tech_companies)

print(companies)

# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}


# Remove an Element from a Set
# We use the discard() method to remove the specified element from a set. For example,

languages = {'Swift', 'Java', 'Python'}

print('Initial Set:',languages)

# remove 'Java' from a set
removedValue = languages.discard('Java')

print('Set after remove():', languages)
#output

# Initial Set: {'Python', 'Swift', 'Java'}
# Set after remove(): {'Python', 'Swift'}

#discra,pop,remoce like all key words
#find duplicate and unique sin set oif number
#all set operstaion union,difrrese,intescation,union

#find duplicat elemt in the set of elemts
num=input("enter numbers: ").split()
l=list(set(num))
dup=" "
uni=" "
for i in l:
  if(num.count(i)>1):
    dup+=i+" "
  else:
    uni+=i+" "
print(dup)
print("duplicates {}".format(dup))
print("uniques {}".format(uni))

#ip--20 10 30 30 40 20 50
#o/p--Output:

# enter numbers:  30 20 
# duplicates  30 20 
# uniques  40 50 10 



#new day -2/1/25-dictioary methids
dictr is the collection of iteams,in the key value pair which are separted bye camms and enclosed with in flower brackets

properties
-ordered
-indexing is possivbel
-duplicates keys are not allowed
-duplicates values are not allowed


scores={
  "englishg":86,
  "maths":35,
  "sci":100,
  "hin":96,
  "tel":100
  
}
print(scores)
print(type(scores))


capti=dict()
print(type(capti))

names=dict(teja="la",s="kin")
print(names,type(names))


country_captials={
  
}






























