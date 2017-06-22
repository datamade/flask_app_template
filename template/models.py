import sqlalchemy as sa

from .database import db

class PersonModel(db.Model):
    __tablename__ = 'person'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False, unique=True)
    email = sa.Column(sa.String, nullable=False, unique=True)
    
    def __repr__(self): # pragma: no cover
        return '<PersonModel %r>' % self.name

