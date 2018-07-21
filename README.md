# Todoist Android Automation

In this project I used pyest and Appium to create automated tests for the Todoist Android app.

## Project Dependencies

* Python3
* Appium

There's also few essentials needed to run the automation. 

1. The Todoist apk file - This file needs to be placed in the apps directory in the src folder
2. The environment(.env) file - This file needs to be placed in the root of the project and should look something like this

```bash
TOKEN=<Your Todoist personal access token>
email=<The email that will be used to sign in>
password=<password for that email>
```

Once you've satisfied those requirements, install the Python dependencies with,

```pip install -r requirements.txt``` 

and I also recommend doing this within a virtualenv

## Running the project 

From the respective modules to be imported properly you'll need to add the 
sources folder to the pythonpath when running. From MAC/Linux you can do this by executing the app with the following command,

```PYTHONPATH=src pytest <absolute/path/to/tests/folder>```

For Windows this [stackoverflow answer](https://stackoverflow.com/questions/4580101/python-add-pythonpath-during-command-line-module-run)
gives more detail on setting up the python path. 