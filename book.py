'''
book.py
'''

class Book:
    def __init__(self, title, is_paperback):
        self.title = title
        self.is_paperback = is_paperback

        if is_paperback:
            self.price = 9.99
        else:
            self.price = 19.99
    
    def __str__(self):
        return self.title
