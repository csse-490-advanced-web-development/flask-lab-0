# CSSE-490-lab-0

Lab 0: Deploying Our First Flask App

## Project Setup


### Cloning and Installing Dependencies

Make sure you have Python 3.9 [installed locally](https://docs.python-guide.org/starting/installation/). To push to Heroku, you'll also need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)).

```sh
$ git clone <repo url>
$ cd lab-0-<your_github_username>

$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Running Locally

```sh
$ FLASK_APP=hello.py flask run --reload
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

The `--reload` flag ensures that the server reloads your code as you make changes.

## Deploying to Heroku

### Creating the Heroku application

```sh
$ heroku create
$ git push heroku main

$ heroku open
```

### Testing in a local Heroku environment

```sh
$ heroku local
```

### Pushing up new updates to the existing application

```sh
$ git push heroku main
```
