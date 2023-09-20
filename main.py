from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    
my_posts = [{"title": "Seoul", "content": "Best Kbbq", "id":1}, 
           {"title": "Rome", "content": "Live like a Local", "id":2}]

# request Get method url: "/"

@app.get("/")
def root():
    return {"message": "Welcome to my API!!!"} #data that gets sent back to the user

@app.get("/posts") #retrieving data
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post:Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000000)
    my_posts.append(post_dict)
    return {"data": post_dict}
#title str, content str