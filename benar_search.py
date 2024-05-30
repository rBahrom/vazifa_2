import random

data = []

for i in range(55):
    data.append(random.randint(10, 1000))

data = list(set(data))
data.sort()
print(data)

search = int(input("Search number : "))

low = 0
high = len(data)-1
count = 0
while True:
    count += 1
    mid = (low + high)//2
    if data[mid] < search:
        low = mid + 1
    elif data[mid] == search:
        print(search)
        print(f"count : {count}")
        break
    elif data[mid] > search:
        high = mid
    else:
        print(f"{search} bunday raqam topilmadi")




