class Book :
    def get_data(self):
        self.title = input('Enter the title of the Book :')
        self.author = input('Enter th author of the Book :')
        self.publisher = input('Enter the publisher :')
        self.isbn = int(input('Enter the ISBN number :'))

    def show_data(self):
        print('Title :',self.title)
        print('Author :',self.author)
        print('Publisher :',self.publisher)
        print('ISBN NO. : :',self.isbn)


b1 = Book()
b1.get_data()
b1.show_data()