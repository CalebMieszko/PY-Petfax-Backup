from flask import (Blueprint, render_template, json)

pets = json.load(open('pets.json', encoding='utf-8'))

bp = Blueprint('pet', __name__, url_prefix='/pets')

# pets page
@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)

# individual pet (show page)
@bp.route('/<int:id>')
def pet(id):
    pet = pets[id-1]
    return render_template('pets/pet.html', pet=pet)