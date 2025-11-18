#lists are container that can store all data types

L1 = ["apple", "computer", 4, True, "python"]

print(L1)
print(L1[0])

#lists are mutable i.e they can be changed or editied
L1[0] = "banana"

print(L1[0])
print(L1[0:3]) 

#adds after the list
L1.append("haha")
print(L1)

#reverses the list
L1.reverse()
print(L1)

#insert
L1.insert(1,5) #insert 5 at index    
print(L1)

#pop
L1.pop(1)
print(L1)

#remove
L1.remove("haha")
print(L1)
