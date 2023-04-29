"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

# from . import db
import jwt
from functools import wraps
from . import app, db, login_manager
import os
from flask import render_template, request, jsonify, send_file, make_response, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from app.models import users, posts,likes, follows
from app.forms import RegisterForm, LoginForm, NewPostForm
from flask_wtf.csrf import generate_csrf
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from functools import wraps
from datetime import datetime, timedelta




def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization', None) # or request.cookies.get('token', None)

        if not auth:
            return jsonify({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'}), 401

        parts = auth.split()

        if parts[0].lower() != 'bearer':
            return jsonify({'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}), 401
        elif len(parts) == 1:
            return jsonify({'code': 'invalid_header', 'description': 'Token not found'}), 401
        elif len(parts) > 2:
            return jsonify({'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}), 401
        

        token = parts[1]
    
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')

        except jwt.ExpiredSignatureError:
            return jsonify({'code': 'token_expired', 'description': 'token is expired'}), 401
        except jwt.DecodeError:
            return jsonify({'code': 'token_invalid_signature', 'description': 'Token signature is invalid'}), 401

        current_user = users.query.filter_by(id = data['user_id']).first()

        return f(current_user, *args, **kwargs)

    return decorated


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/v1/register', methods = ['POST'])
def register():
    form = RegisterForm()
    response = {}

    if request.method=='POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            firstname = form.firstname.data
            lastname = form.lastname.data
            email = form.email.data
            location = form.location.data
            biography = form.biography.data
            profile_photo = form.photo.data
            photo_filename = secure_filename(profile_photo.filename)

            response = jsonify({"message": "User Successfully Added",
                                "username": username,
                                "first Name": firstname,
                                "last Name": lastname,
                                "password" :password,
                                "email" : email,
                                "location": location,
                                "biography":biography,
                                "photo": photo_filename})
            new_user= users(username, password, firstname, lastname, email, location, biography, photo_filename)
            profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))
            db.session.add(new_user)
            db.session.commit()
        
            return make_response(response,200)
        else:
            return make_response({'errors': form_errors(form)},400)




@app.route('/api/v1/auth/login', methods = ['POST'])
def login():
    if request.method=='POST':
        form = LoginForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data

            user = db.session.execute(db.select(users).filter_by(username=username)).scalar()
       
            if user is not None and (check_password_hash(user.password, password)):
                timestamp = datetime.utcnow()
                payload = {
                    "sub": 1,
                    "iat": timestamp,
                    "exp": timestamp + timedelta(minutes=60),
                    "user_id": user.id
                }

                token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
            
                return make_response(jsonify({'token' : token, "message": "Login Successful"}),201)
        else:
            return make_response({'errors': form_errors(form)},400)
       




@app.route("/api/v1/auth/logout", methods=['POST'])
@login_required
def logout():
    logout_user()
    message = {'success':'Successfully logged out'}
    return jsonify(message)

@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(users).filter_by(id=id)).scalar()

@app.route('/api/v1/users/<user_id>/posts', methods = ['POST','GET'])
@login_required
@requires_auth
def showposts(user_id):
    if request.method=='POST':
        form = NewPostForm()
        if form.validate_on_submit():
            caption = form.caption.data
            photo = form.photo.data
            pname = secure_filename(photo.filename)
            newPost = posts(caption, pname, user_id)
            db.session.add(newPost)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], pname))
            db.session.commit()

            return jsonify({"message": "Successfully created a new post"})
        else:
            return make_response({'errors': form_errors(form)},400)
    
    elif request.method == 'GET':
        postl = posts.query.filter_by(user_id=user_id).all()
        pList = []
        for post in postl:
            pList.append({
            "id": post.id,
            "user_id": post.user_id,
            "photo": "/api/v1/photos/{}".format(post.photo),
            "caption": post.caption,
            "created_on": post.created_on
        })
    
        data = {"posts": pList}
        return jsonify(data)




@app.route('/api/v1/users/<user_id>/follow', methods = ['POST'])
@login_required
@requires_auth
def follow(current_user, user_id):
    if request.method=='POST':
        follower_id = current_user
        user_id = user_id
        newFollower = follows(follower_id, user_id)
        db.session.add(newFollower)
        db.session.commit()

        return make_response({"message": "Successfully followed user"},200)
    

# @app.route('/api/v1/posts', methods = ['GET'])
# @requires_auth
# def showposts():
#     postl = posts.query.all()
#     plist = []
#     for post in postl:
#         likel = likes.query.filter_by(post_id=post.id).all()
#         plist.append({
#             "id": post.id,
#             "user_id": post.user_id,
#             "photo": "/api/v1/photos/{}".format(post.photo),
#             "caption": post.caption,
#             "created_on": post.created_on,
#             "likes": likel 
#         })
    
#     data = {"posts": plist}
#     return jsonify(data)


@app.route('/api/v1/posts', methods=['GET'])
@login_required
#@requires_auth
def get_all_posts():
    """Return all posts for all users"""
    postsl = db.session.execute(db.select(posts)).scalars()
    all_posts = []
    for post in postsl:
        likel = db.session.execute(db.select(likes).filter_by(id=post.id)).scalars()
        all_posts.append({
            "id": post.id,
            "user_id": post.user_id,
            "photo": post.photo,
            "caption": post.caption,
            "created_on": post.created_on,
            "likes": len([like for like in likel])
        })
    return jsonify(all_posts), 200


@app.route('/api/v1/posts/<post_id>/like', methods = ['POST'])
@login_required
@requires_auth
def like(post_id):
    if request.method=='POST':
        user_id = current_user
        post_id = post_id
        newLike= likes(post_id, user_id)
        db.session.add(newLike)
        db.session.commit()

        return make_response({"message": "Successfully liked post"},200)



@app.route('/api/v1/photos/<filename>')
@requires_auth
def getPhoto(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)



@app.route('/api/v1/profile_photo/<filename>')
@login_required
@requires_auth
def getProfilePhoto(current_user, filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)


@app.route('/api/v1/csrf-token', methods=['GET']) 
def get_csrf():     
    return jsonify({'csrf_token': generate_csrf()})  


###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

# profile_photo="er"
# new_user= Users("gravl","password","firstname","lastname","t@gmail.com","location","biography","photo_filename")
# profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], profile_photo))
# db.session.add(new_user)
# db.session.commit()