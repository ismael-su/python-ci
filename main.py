# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.get("/")
def test():
    return 'This is just a test, making sure we can run our container'


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


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('RS Server starting')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
