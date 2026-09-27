class UserProfile:

    def __init__(self, first_name, last_name, age, phone_number, work_place, gender, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.work_place = work_place
        self.gender = gender
        self.country = country

    def info(self):
        return (self.first_name, self.last_name, self.age, self.phone_number, self.work_place, self.gender, self.country)

user1 = UserProfile('Асель', 'Асанова', 23, '+9967778838383', 'Optima bank', 'Ж', 'KG')


print(user1.first_name) 
print(user1.info())

class Author:
    def __init__(self, first_name, last_name, age, phone_number, work_place, gender, country, city, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.work_place = work_place
        self.gender = gender
        self.country = country
        self.city = city
        self.height = height

    def info(self):
        return (self.first_name, self.last_name, self.age, self.phone_number, self.work_place, self.gender, self.country, self.city, self.height)
user2 = Author('Асан', 'Аманов', 34, '+9967778838334', 'ЦУМ', 'М', 'KG', 'Бишкек', 190)
print(user2.first_name)  
print(user2.info())
