'''
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
    def get_average_grade(self):
        x = 0
        z = 0
        for i in self.students:
            x += self.students[z].grade
            z += 1
        x = x/len(self.students)
        print(x)
'''
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print (f"i am {self.name} and i am {self.age} years old")

    def speak(self):
        print ("idk what to say")

class Cat(Pet):
    def __init(self, name, age, colour):
        super().__init__(name,age)
        self.colour = colour
    def speak(self):
        print ("meow")

    def show(self):
        print (f"i am {self.name} and i am {self.age} years old and i am {self.colour}")
class Dog(Pet):
    def speak(self):
        print ("bark")
class Dog(Pet):
    pass


p = Pet("Tim", 19)
p.show()
p.speak()
c = Cat("bill", 34, "black")
c.show()
c.speak()

d = Dog("jill", 25)
d.show()
d.speak()




Hao = Student('Hao', 14, 80)
Sean = Student('Sean', 14, 90)
Mike = Student('Mike', 14, 100)
Math = Course('Math', 2)
Math.add_students(Hao)
Math.add_students(Sean)
Math.add_students(Mike)
Math.get_average_grade()
    
