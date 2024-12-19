from datetime import datetime
from pydantic import BaseModel, Field


#patients class
class User(BaseModel):
    name:str
    email:str

#add new user
class Create_user(User):
    userid:int
    is_active:bool|None=Field(default=True)
    

###########################################################
#Books class
class Book(BaseModel):
    title:str
    author:str

#create new book
class Create_book(Book):
    bookid:int
    is_available:bool|None=Field(default=True)


###########################################################
#borrow class
class Borrow(BaseModel):
    intended_return_date:datetime

#borrow a book/books
class Create_borrow(Borrow):
    borrow_id:int
    userid:int
    bookid:int
    borrow_date:datetime
    return_date: datetime | None # type: ignore



#user table
user_db=[Create_user(userid=1, name="James", email="james@example.com", is_active=True),
         Create_user(userid=1, name="John", email="john@example.com", is_active=True),
         Create_user(userid=1, name="Sohn", email="sohn@example.com", is_active=True),
         Create_user(userid=1, name="Jambre", email="jambre@example.com", is_active=True)
         ]

#book table
book_db=[Create_book(bookid=1, title="the dragon flies", author="Francis Galton", is_available=True),
         Create_book(bookid=2, title="More to life", author="Sunnet Dayang", is_available=True),
         Create_book(bookid=3, title="A thousand dreams", author="James Rugger", is_available=True),
         Create_book(bookid=4, title="Never say never", author="Stone Winner", is_available=True),
         ]
#borrowing table
borrow_db=[Create_borrow(borrow_id=1, bookid=4, userid=2, borrow_date=12/12/2024, intended_return_date=17/17/2024, return_date=17/17/2024),
          Create_borrow(borrow_id=2, bookid=2, userid=3, borrow_date=11/11/2024, intended_return_date=16/16/2024, return_date=16/16/2024),
          Create_borrow(borrow_id=3, bookid=1, userid=1, borrow_date=10/10/2024, intended_return_date=15/15/2024, return_date=15/15/2024),
          Create_borrow(borrow_id=4, bookid=3, userid=4, borrow_date=9/9/2024, intended_return_date=14/14/2024, return_date=14/14/2024)
         ]