# for loop
for i in range(1, 6):
    print(i)

s = "varun_patil"

for i in s:
    print(i)


#break and continue

for i in range(50):
    if(i == 45):
        break  # Exit the loop
    print(i)

for i in range(50):
    if(i == 45):
        continue  # Skip this iteration
    print(i)