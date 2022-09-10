# List Built-in methods
# append - clear - copy - count - extend - index - insert - pop - remove - reverse - sort

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
numbers = [2, 3, 5, 2, 11, 2, 7,2,2]
count = numbers.count(2)
print('Count of 2:', count)
print(".....................................")

#5 List --> list1.extend(iterable) :Add the elements of a list (or any iterable), to the end of the current list
list1 = [12, 33, 45]
list2 = [11, 32]
list2.extend(list1)
print('List after extend():',list2)
print(".....................................")
#6 Index--> list.index(elmnt): returns the index of the element in the list
animals = ['cat', 'dog', 'rabbit', 'horse']
index = animals.index('dog')
print(index)
print(".....................................")







ls=[33,44,66,22]
ls.sort()
print(ls)