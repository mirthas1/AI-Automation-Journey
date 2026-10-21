from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get('/')
def get_message():
    return {'message':'Hello API'}

@app.post('/post')
def test_pots(payload: dict= Body(...)):
    print(payload)
    return{'posttest':'posttestsuccessfull'}

@app.post('/testpost')
def test_post1(variable: dict = Body):
    print(variable)
    return{"message":f"title: {variable["title"]} \n content: {variable["content"]}"}