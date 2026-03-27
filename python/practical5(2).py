#defining the function

def str_ops(text):
    print('Upper : ',text.upper())
    print('lower : ',text.lower())
    print('Replacing : ',text.replace('a','@'))
    print('capitalized : ',text.capitalize())
    print('Find : ',text.find('a'))

string=input('Enter a string: ')
str_ops(string)
