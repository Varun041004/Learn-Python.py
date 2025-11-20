#   *
#  ***
# *****
n = int(input("Enter the number :"))
for i in range(1, n+1):
    print(" " * (n-i), end="")       #to print the space before the star for each row and end is for the next print to not to go on a new next line
    print("*" * (2*i-1), end="")    #to print the number of stars in each row
    print("")           #to go to the next line that why not using end
#         print(" " * (rows-i) + "*" * (2*i - 1) )    


# *
# **
# ***
n = int(input("Enter the number :"))

for i in range(1, n+1):
    print("*" * i)


# *****
# ***
# *
n = int(input("Enter the number :"))

for i in range(n, 0, -1):
    print("*" * i)

# ***
# * *
# ***

# ****
# *  *
# *  *
# ****
n = int(input("Enter the number :"))

for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*" * n)
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*")