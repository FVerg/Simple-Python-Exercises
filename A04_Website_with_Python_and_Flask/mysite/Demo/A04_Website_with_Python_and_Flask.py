# Application 4: Website creation

# We are going to create a website in Python, using Flask.
# As you may already know, client side websites are mostly made in HTML and CSS.
# The back-end part, can be written in Python, and we are going to see how.

# Flask is a Python framework which has all the tools to build a website in Python.
# It can be installed by typing pip install flask in a windows Shell.

# We import the class Flask from the flask module. It contains all we need
# We need render_template too: a method which allows us to return an HTML page

from flask import Flask, render_template

# We instantiate the Flask class. Name is the name of the script.
# When we run a Python script, Python automatically assigns to it the name "__main__"
# When the script is imported from another script, it will be assigned its own file name
# in this case A04_Website_with_Python_and_Flask.py

app = Flask(__name__)

# Then we indicate the URL where the website will be run: (/ is home)

# This is a decorator. It indicates that the output of this code will be saved
# in the path indicated. localhost:5000 is implicit.

# @app.route('/')

# Now we are going to write some standard code to let the website run

# In this function goes the code of the homepage
# We can return HTML files instead than strings.

# def home():
#     return "Website content goes here!"

# Let's create another page, accessible as "localhost:5000/about"

# @app.route('/about/')

# def about():
#     return "About content goes here!"

# If the script is executed and not imported from another one:
# if __name__ == "__main__":
#     app.run(debug=True)

# At this point, executing the script, we can access to our almost empty website
# by typing in the browser "localhost:5000"

# We want now import an HTML file in our Python function.
# I already provided two HTML pages in the templates folder.
# It is mandatory to put the HTML files into a folder called "templates"
# otherwise it won't work.

@app.route ('/')

def home():
    return render_template("home.html")

@app.route('/about/')

def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

# If you want to add a CSS you need to put the CSS file in the static folder
# otherwise Python won't find it.

# After having worked on the HTML and CSS files, we want to deploy the website on the web.
# We are going to deploy it on heroku, which is free.

# To do this, it is a better practice to install a Python virtual environment:
# pip install virtualenv

# Then, to create a virtual environment, in the main folder of the project we
# create a folder (in our case "mysite") and into it we execute:
# python -m venv virtual
# A folder called virtual will be created, and inside it there will be
# a separated installation of Python.

# To run the just installed version of Python we run:
# .\virtual\Scripts\python

# We install flask in our new Python environment:
# virtual\Scripts\pip install flasks

# And then we run the script by doing:
# virtual\Scripts\python Demo\A04_Website_with_Python_and_Flask

# Before creating any flask application is strongly recommended to create
# a virtual environment!!

# We need to deploy the website on Heroku.
# It has to be done from the command line.

# Step 1: Create a Heroku account
# Step 2: Download and install Heroku toolbelt (allows to communicate with Heroku server through cmd)
# Step 3: Open the cmd from the folder in which this script is saved (Demo in our case)
#         and login typing  "heroku login" and insert credentials
# Step 4: Create a new web app by typing: "heroku create appname"
#         I named it fvergwebsite, so I will use this name from now on.
#         We can now access to our application by surfing to fvergwebsite.herokuapp.com
# Step 5: Install gunicorn in the Python virtual environment (pip install gunicorn).
#         Python will need it to run our web app.
# Step 6: Create in the Demo folder files: 1. requirements.txt (dependencies) heroku
#         has to install (like flask)
# Step 6: Put the dependencies in the requirements.txt (virtual\Scripts\pip freeze > requirements.txt)
# Step 7: Create a Procfile in the Demo folder. It must have no extension. It will tell
#         heroku which web server will run the application. We put inside the file the line:
#         web: gunicorn A04_Website_with_Python_and_Flask:app
#         to tell heroku we are using gunicorn and we want to run the indicated script.
# Step 8: Create a runtime.txt file. It will contain the python version to run the heroku app.
