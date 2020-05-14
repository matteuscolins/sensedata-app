import functools
from models.starship import Starship
from flask_paginate import Pagination, get_page_args
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

bp = Blueprint('starship', __name__, url_prefix='/starship')

starships = Starship.get_all()

def get_starship(offset=0, per_page=10):
    return starships[offset: offset + per_page]

@bp.route('/', methods=('GET', 'POST'))
def home():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')   
    total=len(starships)
    pagination_starship = get_starship(offset=offset, per_page=per_page)
    pagination = Pagination(page = page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('starship/starship.html', starship = pagination_starship, page = page, 
                                                pagination=pagination, per_page=per_page)

@bp.route('/orderByName', methods=('GET', 'POST'))
def order_ny_name():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')   
    starships.sort(key=lambda x: x.name)
    total=len(starships)
    pagination_starship = get_starship(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('starship/starship.html', starship = pagination_starship, 
                    page = page, pagination=pagination, per_page=per_page)

@bp.route('/orderByGender', methods=('GET', 'POST'))
def order_by_gender():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')   
    starships.sort(key=lambda x: x.gender)
    total=len(starships)
    pagination_starship = get_starship(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('starship/starship.html', starship = pagination_starship, 
                    page = page, pagination=pagination, per_page=per_page)

@bp.route('/orderByMass', methods=('GET', 'POST'))
def order_by_mass():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')   
    starships.sort(key=lambda x: x.mass)
    total=len(starships)
    pagination_starship = get_starship(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('starship/starship.html', starship = pagination_starship, 
                    page = page, pagination=pagination, per_page=per_page)

@bp.route('/orderByHeight', methods=('GET', 'POST'))
def order_by_height():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')   
    starships.sort(key=lambda x: x.height)
    total=len(starships)
    pagination_starship = get_starship(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('starship/starship.html', starship = pagination_starship, 
                    page = page, pagination=pagination, per_page=per_page)