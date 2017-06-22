from flask import Blueprint, render_template, redirect, url_for, flash

from .models import PersonModel
from .forms import PersonForm
from .database import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    form = PersonForm()

    if form.validate_on_submit():
        
        person = PersonModel(name=form.data['name'],
                             email=form.data['email'])
        db.session.add(person)
        db.session.commit()

        flash('Person {} saved!'.format(person.name))
    
    return render_template('index.html', form=form)

@views.route('/about/')
def about():
    return render_template('about.html')

