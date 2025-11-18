#string is always imutable 
name = "Varun"

#creating a short str
name_short = name[0:3]
print(name_short)

#printing a particular char
char = name[1]
print(char)

#also there is negative slicing
print(name[-4:-2])
#which is same as 
print(name[1:3])

print(name[:4]) #is same as [0:4]
print(name[2:]) #is same as [2:len]

a = 'amazing'
print(a[1:6:2]) #this prints mzn