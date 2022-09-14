# List Built-in methods
# 1ppend -2 clear -3 copy -4 count -5 extend -6 index -7 insert -8 pop -9 remove -10 reverse -11 sort

#1 append -->list.append(item)  --> Add a single element to the end of the list.

list=[['adam',33],['aram',44],[33,'hare,']]
print(list[1][1])
list.append(333)
print(list)
print(".....................................")
#2 Clear -->  list.clear() : Removes all Items from the List
list=[['adam',33],['aram',44],[33,'hare,']]
print(list.clear())
print(".....................................")
#3 Copy -->  list.copy() : returns a shallow copy of the list
list=[['adam',33],['aram',44],[33,'hare,']]
lis2=list.copy()
print(lis2)
print(".....................................")
#4 count -->  list.count(element) : returns count of the element in the list
print('count')
numbers = [2, 3, 5, 2, 11, 2, 7,2,2]
count = numbers.count(2)
print('Count of 2:', count)
print(".....................................")

#5 List --> list1.extend(iterable) :Add the elements of a list (or any iterable), to the end of the current list
print('extend')
list1 = [12, 33, 45]
list2 = [11, 32]
list2.extend(list1)
print('List after extend():',list2)
print(".....................................")
#6 Index--> list.index(elmnt): returns the index of the element in the list
print('indexing')
animals = ['cat', 'dog', 'rabbit', 'horse']
index = animals.index('dog')
print(index)
print(".....................................")

#7 insert
print('insert')
a=["Red", "Blue", "Green", "Black"]
a.insert(2,'adam')
print(a)
print(".....................................")
#modify
print('modify')
a=["Red", "Blue", "Green", "Black"]
a[1]='grey'
print(a)
print(".....................................")
#8 Pop is to remove an item at the given position in the list
print('Pop')
a=["Red", "Blue", "Green", "Black"]
s=a.pop(1)
print(s)
print(a)
print(".....................................")
#9 remove an item from the list
print('remove')
a=["Red", "Blue", "Green", "Black"]
a.remove('Blue')
print(a)
print(".....................................")
#remove all items from the list
print('clear')
a=["Red", "Blue", "Green", "Black"]
print(a)
a.clear()
print(a)
print(".....................................")
#10 Slicing
print('slicing')
print(".....................................")

# how to print the indexing of all elements from a list
#1
#example 1
a=[1, 5, 7, 3, 2, 4, 6]
print(len(a))
print(a)
for i in range(len(a)):
    print( i ," ",a[i])
#example2

a=[*range(34,51)]
print(len(a))
for i in range(len(a)):
    print(i,"",a[i])

#2 enumerate function
print('\n enumerate')
a=[*range(34,51)]
for i,j in enumerate(a):
    print(i,'',j)

print("\n enumerate with tuple")
s=tuple(enumerate(a))
print(s)

print("\n enumerate with list")
for i in enumerate([*range(12,25)]):
    print(i)







