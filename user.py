from httpx import delete
from models import User, Create_user, Borrow, Create_borrow, book_db, user_db, borrow_db
from fastapi import HTTPException, APIRouter

from datetime import datetime

router=APIRouter()



#create new user
@router.post("api/v1/user/new_user/", status_code=201)
async def create_user(user:User):
    i=0
    while i<len(user_db):
        for user in user_db:
            if user.email!=user.email:
                id=len(user_db)+1
                new_user:Create_user=Create_user(id=id, is_active=True, **user.model_dump())
                user_db.append(new_user)
            else:
                raise HTTPException(status_code=422, detail="User Already Exists")
    

#deactivate user with the id=userid
@router.patch("api/v1/user/{userid}", status_code=204)
async def deactivate_user(userid): #, patch_user: Patched_user
    for i, user in enumerate(user_db):
        if user.userid==userid:
            user_db[i].is_active=False
            #return{"status_code":response, "message":"User inactive"}

            #or
            #user_db[i]=patch_user

        else:
            raise HTTPException(status_code=404, detail="User Not found")


#borrow a book (note that return_date is empty and will only be updated when the book is returned
#we could also detect borrowers who are consistent with returning borrowed books promptly; 
#if return_date is equal or less than the intended_return_date)
@router.get("api/v1/book/{userid}/{bookid}", status_code=200)
async def borrow_book(userid, bookid, borrow:Borrow):
    for i, book in enumerate(book_db):
        for user in user_db:

            #check book availability and user activity
            if (book.bookid==bookid and book.is_available==True):
                if(user.userid==userid and user.is_active==True):
                    id=len(borrow_db)+1
                    new_borrow:Create_borrow=Create_borrow(borrow_id=id, bookid=bookid, userid=userid, borrow_date=datetime.now(), **borrow.model_dump())
                    borrow_db.append(new_borrow)
                    book_db[i].is_available=False
                    return{"message":"Borrowing Successful"}
                else:
                    raise HTTPException(status_code=423, detail="Your access is currently limited to borrowing")
            else:
                raise HTTPException(status_code=404, detail="Book is currently unavailable")


#return borrowed book
@router.post("api/v1/book/{bookid}/{borrowid}", status_code=204)
async def return_book(bookid, borrowid):
    #update return date
    for i, borrow in enumerate(borrow_db):
        if borrow.borrow_id==borrowid:
            borrow_db[i].return_date=datetime.time()

            #update the book availability
            for b, book in enumerate(book_db):
                if book.bookid==bookid:
                    book_db[b].is_available=True
                    return{"message":"Book return was successful!"}
        else:
            raise HTTPException(status_code=422, detail="The operation can not be performed on the item")

#view user's borrowing record
@router.get("api/v1/book/{userid}/", status_code=200)
async def borrow_record(userid):
    i=0
    while i<len(borrow_db):
        for borrow in borrow_db:
            if borrow.userid==userid:
                return borrow
            else:
                raise HTTPException(status_code=404, detail="No records found for the user")