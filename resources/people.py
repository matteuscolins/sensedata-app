import functools
from models.people import People
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

bp = Blueprint('people', __name__, url_prefix='/people')

@bp.route('/', methods=('GET', 'POST'))
def home():
    data = People.get_all()
    data.sort(key=lambda x: x.name, reverse=False)
    return render_template('people/people.html', people = data)