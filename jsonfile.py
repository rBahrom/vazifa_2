import json


def files():
    web = input(f"""
            1.  Register
            2.  Benar search
             >>>>>>>>>>> """)
    if web == '1':
        return register()
    elif web == '2':
        return
    else:
        print("Input Error")
        return file()


def register():
    """
    Bu yerda json file uchun register
    :return:
    """
    print("Welcome to register page")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = int(input("Age: "))
    user = User(first_name, last_name, age)
    user.save()
    return files()


class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return (f"{self.first_name} "
                f"{self.last_name} "
                f"{self.age}")

    def save(self):
        with open("baza.json", encoding="utf-8") as file:
            data = json.load(file)

        with open("baza.json", "w") as f:
            users = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
            data["search"].append(users)
            json.dump(data, f, indent=6)
        print("Foydalanuvchi json file qo'shildi")
        return files()


def search():
    searchs = input("Search: ")
    count = 0
    low = 0
    while True:
        count += 1
        with open("baza.json", encoding="utf-8") as file:
            data = json.load(file)
            high = len(data) - 1
            mid = (low + high) // 2
            if data[mid] < searchs:
                low = mid + 1
            elif data[mid] == searchs:
                print(searchs)
                print(f"count : {count}")
                break
            else:
                print(data[mid])


if __name__ == '__main__':
    files()
