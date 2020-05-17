import functools
from models.people import People
from models.film import Film
from models.vehicle import Vehicle
from models.starship import Starship
from models.planet import Planet
from flask_paginate import Pagination, get_page_args
from flask import (Blueprint, render_template, request)

bp = Blueprint('people', __name__, url_prefix='/people')

people = People.get_all()


def get_people(offset=0, per_page=10):
    return people[offset: offset + per_page]


@bp.route('/', methods=('GET', 'POST'))
def home():
    try:
        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
        total=len(people)
        pagination_people = get_people(offset=offset, per_page=per_page)
        pagination = Pagination(page = page, per_page=per_page, total=total,
                                css_framework='bootstrap4')
        return render_template('people/people.html', people = pagination_people, page = page,
                                                    pagination=pagination, per_page=per_page)
    except:
        return {'message': 'Server Error'}


@bp.route('/orderByName', methods=('GET', 'POST'))
def order_by_name():
    try:
        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
        people.sort(key=lambda x: x.name)
        total=len(people)
        pagination_people = get_people(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                                css_framework='bootstrap4')
        return render_template('people/people.html', people = pagination_people,
                        page = page, pagination=pagination, per_page=per_page)
    except:
        return {'message': 'Server Error'}


@bp.route('/orderByGender', methods=('GET', 'POST'))
def order_by_gender():
    try:
        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
        people.sort(key=lambda x: x.gender)
        total=len(people)
        pagination_people = get_people(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                                css_framework='bootstrap4')
        return render_template('people/people.html', people = pagination_people,
                        page = page, pagination=pagination, per_page=per_page)
    except:
        return {'message': 'Server Error'}


@bp.route('/orderByMass', methods=('GET', 'POST'))
def order_by_mass():
    try:
        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
        people.sort(key=lambda x: x.mass)
        total=len(people)
        pagination_people = get_people(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                                css_framework='bootstrap4')
        return render_template('people/people.html', people = pagination_people,
                        page = page, pagination=pagination, per_page=per_page)
    except:
        return {'message': 'Server Error'}


@bp.route('/orderByHeight', methods=('GET', 'POST'))
def order_by_height():
    try:
        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
        people.sort(key=lambda x: x.height)
        total=len(people)
        pagination_people = get_people(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                                css_framework='bootstrap4')
        return render_template('people/people.html', people = pagination_people,
                        page = page, pagination=pagination, per_page=per_page)
    except:
        return {'message': 'Server Error'}


@bp.route('/filter', methods=('GET', 'POST'))
def filter_people():
    try:
        people_filtered = []
        description = request.form['description']
        type_filter = request.form['filter']
        if type_filter == 'film':
            people_filtered = filter_by_film(description)
        if type_filter == 'vehicle':
            people_filtered = filter_by_vehicle(description)
        if type_filter == 'starship':
            people_filtered = filter_by_starship(description)
        if type_filter == 'planet':
            people_filtered = filter_by_planet(description)
        
        page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page') 
        total=len(people_filtered)
        pagination_people = get_people(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                                css_framework='bootstrap4')
        return render_template('people/people.html', people = people_filtered, 
                        page = page, pagination=pagination, per_page=per_page)
    except:
        return {'message': 'Server Error'}


def filter_by_film(description):
    try:
        films = Film.get_all()
        films_filtered = []
        people_filtered = []
        for i in range(len(films)):
            if description.lower() in films[i].title.lower():
                films_filtered.append(films[i])

        if films_filtered is not None:
            for i in range(len(films_filtered)):
                for j in range(len(people)):
                    for k in range(len(people[j].films)):
                        if people[j].films[k] == films_filtered[i].url:
                            people_filtered.append(people[j])

        return people_filtered
    except:
        return {'message': 'Server Error'}


def filter_by_vehicle(description):
    try:
        vehicles = Vehicle.get_all()
        vehicles_filtered = []
        people_filtered = []
        for i in range(len(vehicles)):
            if description.lower() in vehicles[i].name.lower():
                vehicles_filtered.append(vehicles[i])

        if vehicles_filtered is not None:
            for i in range(len(vehicles_filtered)):
                for j in range(len(people)):
                    for k in range(len(people[j].vehicles)):
                        if people[j].vehicles[k] == vehicles_filtered[i].url:
                            people_filtered.append(people[j])

        return people_filtered
    except:
        return {'message': 'Server Error'}


def filter_by_starship(description):
    try:
        starships = Starship.get_all()
        starships_filtered = []
        people_filtered = []
        for i in range(len(starships)):
            if description.lower() in starships[i].name.lower():
                starships_filtered.append(starships[i])

        if starships_filtered is not None:
            for i in range(len(starships_filtered)):
                for j in range(len(people)):
                    for k in range(len(people[j].starships)):
                        if people[j].starships[k] == starships_filtered[i].url:
                            people_filtered.append(people[j])

        return people_filtered
    except:
        return {'message': 'Server Error'}


def filter_by_planet(description):
    try:
        films = Film.get_all()
        planets = Planet.get_all()
        people = People.get_all()

        planets_filtered = []
        films_filtered = []
        people_filtered = []

        for i in range(len(planets)):
            if description.lower() in planets[i].name.lower():
                planets_filtered.append(planets[i])

        if planets_filtered is not None:
            for i in range(len(planets_filtered)):
                for j in range(len(films)):
                    for k in range(len(films[j].planets)):
                        if films[j].planets[k] == planets_filtered[i].url:
                            films_filtered.append(films[j])

        for i in range(len(films_filtered)):
            for j in range(len(people)):
                for k in range(len(people[j].films)):
                    if people[j].films[k] == films_filtered[i].url:
                        people_filtered.append(people[j])

        return people_filtered
    except:
        return {'message': 'Server Error'}
