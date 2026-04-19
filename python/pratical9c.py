# Name and Roll No
print("Name: Mangesh Mahajan")
print("Roll No: FIB48")

class Student:
    def __init__(self, name, roll, marks):
        # Public members
        self.name = name
        self.roll = roll
        
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)
        print("Marks:", self.__marks)
        print("----------------------")

s1 = Student("Rahul", 1, 85)
s2 = Student("Sneha", 2, 90)
s3 = Student("Amit", 3, 78)

print("Accessing Public Members:")
print(s1.name, s1.roll)

print("\nAccessing Private Member using Getter:")
print("Marks of Rahul:", s1.get_marks())

s1.set_marks(88)

print("\nStudent Details:")
s1.display()
s2.display()
s3.display()