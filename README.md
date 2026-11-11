# 11-2class

## prerequisites

Install python version 3.x (i.e. using Anaconda)

## setup

some instructions here

1. clone [the repo](https://github.com/hayeon3683/11-2class) from GitHub, and put it somewhere like your Desktop
2. navigate to the local repo from the command line (e.g., if on your desktop):

```sh
cd ~/Desktop/mt-first-app-fall-2026
```
3. create a new anaconda virtual environment called "rps-env" first time only:

```sh
conda create -n rps-env python=3.11
```

4. activate the virtual environment as ncessary every time come back to the project

```sh
conda activate rps-env

5. install packag dependencies:

```sh
pip install -r requirements.txt

make sure the Anaconda base environment is active


# can help future u, collaborators, AI agents

## usage

## command line app

## web app 
### Web App

```sh
# if we have the FLASK_APP=web_app env var in the ".env" file:
flask run

# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run



some commands here to run the files

Run the example script

```sh
 python app/my_script.py

# alternatively:
python - m app.my_script

```sh
 python app/rps.py

 python - m app.rps




# maybe have to change the name as well


#Testing

to run tests:

```sh
pytest
```