from models import Create_book, Book, book_db
from fastapi import  HTTPException, APIRouter

router=APIRouter()


#create new user
@router.post("api/v1/book/new_book/", status_code=201)
async def create_user(book:Book):
    i=0
    while i<len(book_db):
        for book in book_db:
            if book.title!=book.title:
                id=len(book_db)+1
                new_book:Create_book=Create_book(id=id, is_active=True, **book.model_dump())
                book_db.append(new_book)
                return {"message":"Registration successful"}
            else:
                raise HTTPException(status_code=422, detail="User Already Exists")

#mark book as unavailable   
@router.patch("api/v1/book/{bookid}", status_code=200)
async def unavailable_book(bookid):
    for i, book in enumerate(book_db):
        if book.userid==bookid:
            book_db[i].is_available=False
            return{"message":"book unavailable"}
        else:
            raise HTTPException(status_code=404, detail="Book does not exist")


