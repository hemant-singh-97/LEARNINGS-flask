from flask import Flask

app = Flask(__name__)

@app.route('/') # Accessed using 127.0.0.1:5000/
def hello_world():
    return 'Hello, World!'

@app.route('/about/<username>') # Accessed using 127.0.0.1:5000/about/SOME-NAME (For example 127.0.0.1:5000/about/John)
def about_page(username: str):
    return f"<h1>About Page of {username}</h1>"

# terminal commands :
# export FLASK_APP=hello.py
# export FLASK_DEBUG=1 => Realtime Changes on reload, good for development but bad for production
# flask run