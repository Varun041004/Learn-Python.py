# 5! = 1x2x3x4x5

n = int(input("Enter the number :"))
result = 1
for i in range(1, n+1):
    result = result * i

print(f"Factorial of {n} is {result}")