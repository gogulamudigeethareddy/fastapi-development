from fastapi import FastAPI
from fastapi import Body, FastAPI

app = FastAPI()

##Path operation
@app.get("/")   ##decorator
async def root():
    return {"message": "Welcome to API!!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}


