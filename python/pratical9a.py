class Student :
    def __init__(self,name,age,roll_no,division):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.division =division

    def show_data(self):
        print('Name :',self.name)
        print('Age :',self.age)
        print('Roll Number :',self.roll_no)
        print('Division :',self.division) 
    
    def __del__(self):
        print('del is called')

s1= Student('mangesh',18,48,'b')

s1.show_data()
del s1