from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/<name>')
def Para_app(name):
    return f'Hello {escape(name)} and welcome to my paralympics app'


# Run the app
if __name__ == '__main__':
    app.run(debug=True)