import random

data = []
for i in range(20):
    data.append(random.randint(10, 100))
print(list(set(data)))
target = int(input("Enter a number: "))
count = 0
for j in data:
    count += 1
    if j == target:
        print(j)
        print(count)
        break
    else:
        print(f"{j} Bunday topilmadi")
