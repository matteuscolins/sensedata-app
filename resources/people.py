import functools
from models.people import People
from flask_paginate import Pagination, get_page_args
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

bp = Blueprint('people', __name__, url_prefix='/people')

people = People.get_all()

def get_people(offset=0, per_page=10):
    return people[offset: offset + per_page]

@bp.route('/', methods=('GET', 'POST'))
def home():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')   
    people.sort(key=lambda x: x.name, reverse=False)
    total=len(people)
    pagination_people = get_people(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('people/people.html', people = pagination_people, page = page, pagination=pagination, per_page=per_page)