
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def test():
    return 'Hello World'


@app.get("/users/dev")
def get_devs():
    dev_list = [
        'Joris',
        'Ismael',
        'Lucas',
    ]
    response = {
        'data': dev_list
    }
    return response
