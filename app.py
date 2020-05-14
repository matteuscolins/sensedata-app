from flask import Flask
from resources import people, starship

app = Flask(__name__)

app.register_blueprint(people.bp)
app.register_blueprint(starship.bp)

if __name__ == '__main__':
    app.run(debug=True)