
This project is a showcase of how we can implement a CI/CD workflow on a fastApi based project ran in
a [Docker](https://docs.docker.com/get-started) container
The base [FastAPI Image](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker)

## Run the docker image



### Clone the project

```shell script
git clone https://github.com/Rumble-Studio/python-ci
cd python-ci
python3 -m venv venv
pip install -r requirements.txt
````


# follow instructions from above command


### Build locally and run`

`````shell script
docker build -t myimage .
docker run -d --name rs -p 0.0.0.0:8080:2376/tcp myimage
`````

### Pull image from github package and run locally
#### Note that the login is required for this step

`````shell script
docker login -u {github_username} -p {[token](https://github.com/settings/tokens)} docker.pkg.github.com
docker pull docker.pkg.github.com/rumble-studio/python-ci/ismael-fastapi:latest
docker run -d --name rs -p 0.0.0.0:8080:2376/tcp docker.pkg.github.com/rumble-studio/python-ci/ismael-fastapi:latest
`````


## CI / CD Workflows and Linting/Testing

Before each commit i run some githooks you will find under .github directory

### pre-commit

`````shell script
pip freeze > requirements.txt
git add requirements.txt
autopep8 --in-place --aggressive --aggressive ./app/*.py
flake8 . --count  --show-source --s
pytest
`````


This script invokes autopep8 that automatically formats Python code to conform to the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
Flake8 which is a great toolkit for checking your code base against coding style (PEP8), programming errors (like “library imported but unused” and “Undefined name”).
Pytest is a python framework for running unit test. the test file for this project is under app/test_index file

### github actions

Under .github/workflows/ci-cd.yml there are github actions that run on each push and pull request.
They test the project against 3 different version of python (3.7, 3.8, 3.9), runs autopep8, flake8 , run the tests.
If everything passes, it then pushes the image to github public container registry then prints the docker iamge url as output