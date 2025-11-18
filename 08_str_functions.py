name = 'varun is a new legend in python'

print(len(name))
print(name.endswith("un"))
print(name.startswith("va"))
print(name.capitalize()) #just the starting letter
print(name.upper())
print(name.lower())

print(name.find("legend")) #prints index

#replace
print(name.replace("legend", "king"))

#esc seq
a = "varun is a good boy\nbut not bad \"bouy\"" #u can also use ''

print(a)

#this is called a f func
b = "Varun"
print(f"Good night {b}")

