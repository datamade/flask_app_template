from .database import Base, db_session as session
from flask_bcrypt import Bcrypt
from sqlalchemy import Integer, String, Boolean, Column
from sqlalchemy.orm import synonym

bcrypt = Bcrypt()

class User(Base):
    __tablename__ = 'app_user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    _password = Column('password', String, nullable=False)
    
    def __repr__(self): # pragma: no cover
        return '<User %r>' % self.name

    def _get_password(self):
        return self._password
    
    def _set_password(self, value):
        self._password = bcrypt.generate_password_hash(value)

    password = property(_get_password, _set_password)
    password = synonym('_password', descriptor=password)

    def __init__(self, name, email, password):
        self.name = name
        self.password = password
        self.email = email

    @classmethod
    def get_by_username(cls, name):
        return session.query(cls).filter(cls.name == name).first()

    @classmethod
    def check_password(cls, name, value):
        user = cls.get_by_username(name)
        if not user: # pragma: no cover
            return False
        return bcrypt.check_password_hash(user.password, value)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

