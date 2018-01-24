from flask import Flask

app = Flask(__name__)



@app.route("/")
def index():
    """Home route handler."""
    page = """
    <!DOCTYPE html>
    <html>

    <head>
        <title></title>
    </head>

    <body>
    <h1>Welcome!</h1>

    </body>

    </html>
    """