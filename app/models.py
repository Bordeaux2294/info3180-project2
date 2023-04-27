# Add any model classes for Flask-SQLAlchemy here
from . import db
import pytz
from datetime import datetime
from werkzeug.security import generate_password_hash

class Users(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(128))
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(120))
    location = db.Column(db.String(120))
    biography = db.Column(db.String(255))
    profile_photo = db.Column(db.String(100))
    joined_on = db.Column(db.DateTime)
    
    def __init__(self, id, username, password, firstname, lastname, email, location, biography, profile_photo):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.email = email
        self.id= id
        self.location = location
        self.biography = biography
        self.profile_photo = profile_photo
        time = datetime.now(pytz.timezone('US/Eastern'))
        self.joined_on = time

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
    
class Posts(db.Model):
    __tablename__ = 'Posts'

    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(125))
    photo = db.Column(db.String(125))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", backref="user")
    created_on = db.Column(db.DateTime)

    def __init__(self, id, caption, photo, user_id):
        self.id= id
        self.caption = caption
        self.photo = photo
        self.user_id = user_id
        time = datetime.now(pytz.timezone('US/Eastern'))
        self.created_on = time

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<post: %r>' % (self.id)

class Likes(db.Model):
    __tablename__ = 'Likes'