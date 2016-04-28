from Q4Moudle import UnorderedList
mylist = UnorderedList()

print(mylist.isEmpty())
mylist.add(1234)
mylist.add('pig')
mylist.add(1024)
print(mylist.size())        #['melon',3323,1024] This order may not be
mylist.append(7777)
print(mylist.search(7777))   #['melon',3323,1024,555]
print(mylist.size())
mylist.remove(1024)         #['melon',3323,555]
print(mylist.size())
print(mylist.index(7777))
mylist.insert(2,33)         #['melon',3323,44,555]
print(mylist.index(33))
mylist.pop()                #['melon',3323,44]
print(mylist.search(7777))
mylist.pop(1)               #['melon',44]
print(mylist.search(1234))
