from fastapi import FastAPI
import book, user

app=FastAPI()

@app.get("/home")
async def home():
    return {"message":"The path is working"}

app.include_router(book.router)
app.include_router(user.router)
