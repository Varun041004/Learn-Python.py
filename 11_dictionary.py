#dictionary stores a key value pair 
#there can be list in dict
#dicts are mutable 
d = {
    #this is an empty dictionary
}

marks = {
    "varun":100,
    "yash":99,
    "walse":98,
    "jai":97
}

print(marks, type(marks))
print(marks["jai"]) #but u cant do marks[0]

#prints just keys
print(marks.keys())

#mutable
marks.update({"varun":90})
print(marks)

print(marks.get("varun2"))   #this gives none 
print(marks["varun2"])       #this gives error 