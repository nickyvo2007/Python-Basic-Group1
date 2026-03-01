class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

# Khởi tạo đối tượng
dog = Dog()
cat = Cat()

# Gọi hàm kiểm tra
animal_sound(dog)
animal_sound(cat)