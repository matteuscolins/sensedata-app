from flask import Flask
from resources import people

app = Flask(__name__)

app.register_blueprint(people.bp)

if __name__ == '__main__':
    app.run(debug=True)