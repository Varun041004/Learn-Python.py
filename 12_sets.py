#this is an empty set
e = set()

#no elements can be repeted in set 
#sets are unindexed 
s = {1, 4, 5}

s.add(0)
print(s, type(s))

s.remove(5)
print(s, type(s))

s1 = {1, 4, 5}
s2 = {1, 4, 99, 33, 2, 0}

print(s1.union(s2))
print(s1.intersection(s2))