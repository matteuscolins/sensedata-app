from flask import Flask
from resources.people import bp as bp_people
from resources.starship import bp as bp_starship

app = Flask(__name__)

app.register_blueprint(bp_people)
app.register_blueprint(bp_starship)

if __name__ == '__main__':
    app.run(debug=True)