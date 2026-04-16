class Book :
    a = 'public member'
    _b = 'private member'
    __c = 'protected member'

    def __init__(self):
        print(f"public member :{a}")
        print(f"private member :{_b}")
        print(f"protected member :{__c}")

class Notbook:
    def __init__(self):
        print(f"public member in anoter class :{a}")
    
class Report (Book):
    def __init__(self):
        print(f"public member in derived class :{a}")
        print(f"private member in derived class :{_b}") 

obj = Book()
obj2= Notbook()
obj3 = Report()