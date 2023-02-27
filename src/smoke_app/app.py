from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {'Message': 'Start'}


@app.get('/{id}')
def get_item(pk: int, name: str = None):
    return {"id": pk, "name": name}


@app.get('/user_id/{user_id}/items/')
def get_user_item(user_id: int, item: str = None):
    return {"key": user_id, "item": item}
