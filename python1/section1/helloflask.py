"""A simple flask website that greets people"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def generic():
    """Returns a simple greeting"""
    return "Hi there!"

@app.route("/<name>")
def specific(name):
    """Returns a more specific greeting, with a twist"""
    if name == "Ryan":
        return "Behold, the excellent one!  Master of time and space!"
    else:
        return "Hi {}!  You're pretty fancy!".format(name)

if __name__ == "__main__":
    app.run()
