import sqlalchemy as sa

from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms.validators import DataRequired, Email

from .models import PersonModel
from .database import db

class PersonForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        user = db.session.query(PersonModel)\
            .filter(sa.func.lower(PersonModel.email) == sa.func.lower(self.email.data))\
            .first()

        if user:
            self.email.errors.append('Email address is registered')
        
        user = db.session.query(PersonModel)\
            .filter(sa.func.lower(PersonModel.name) == sa.func.lower(self.name.data))\
            .first()
        
        if user:
            self.name.errors.append('Name is registered')
        
        if self.errors:
            return False

        return True
