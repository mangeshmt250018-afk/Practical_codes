class Collage:
    collage_name ='I2IT PUNE' #class variable

    def __init__(self,name):
        self.name = name #object variable 
   
    
obj = Collage('mangesh')
print(f'Class variable :{obj.collage_name}')
print(f'Object variable :{obj.name}')
