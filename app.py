from flask import Flask, render_template
from flask_cors import CORS
from resources.people import bp as bp_people
from resources.starship import bp as bp_starship


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


app.register_blueprint(bp_people)
app.register_blueprint(bp_starship)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')