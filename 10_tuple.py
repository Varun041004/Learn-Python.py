#tuples are immutable
t = (1, 4,False, 5, 6989, "varun", False)
print(type(t))

tnew = t.count(False)
print(tnew)

#returns index of false
print(t.index(False))

print(t.count(False))

print(t)

print(len(t))