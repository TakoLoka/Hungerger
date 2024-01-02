from flask import Blueprint, render_template, request, session, redirect


users_controller = Blueprint('users_controller', __name__,
                        template_folder='../views', static_folder="../static")

from models.users import *
from models.recipes import *
from models.ingredients import *

def get_path():
    path = request.root_url.replace('/?','')
    return path
    
def column(matrix, i):
    return [row[i] for row in matrix]

@users_controller.route('/login')
def login():
    if 'user_id' in session:
        return redirect('/')
    else:
        print(request.root_url)
        return render_template('login.html')

@users_controller.route('/register')
def register():
    if 'user_id' in session:
        return redirect('/')
    else:
        return render_template('register.html')

@users_controller.route('/login_validation', methods=['POST'])
def login_validation():
    name = request.form.get('name')
    password = request.form.get('password')
    reg_user = validate_user_db(name, password)
    if len(reg_user)>0:
        session['user_id'] = reg_user[0][0]
        return redirect('/')
    else:
        return redirect('/login')

@users_controller.route('/add_user', methods=['POST'])
def add_user():
    first_name=request.form.get('first_name')
    last_name=request.form.get('last_name')
    username=request.form.get('username')
    email=request.form.get('email')
    password=request.form.get('password')
    add_user(first_name, last_name, username,email,password)
    return redirect('/login')

@users_controller.route('/update-profile', methods=['POST'])
def update_profile():
    if 'user_id' in session:
        first_name=request.form.get('first_name')
        last_name=request.form.get('last_name')
        email=request.form.get('email')
        bio=request.form.get('bio')
        user_id = session['user_id']
        update_user(first_name, last_name, email,bio, user_id)
        return redirect('/')
    else:
        return redirect('/login')

@users_controller.route('/user/@<path:user_id>')
def user(user_id):
    if 'user_id' in session:
        path = get_path()
        res = get_user(user_id)
        user = get_user(session['user_id'])
        if len(res) > 0:
            recipes = get_recipes(res[0][1])
            return render_template('profile.html', res = res, user = user, recipes = recipes, path=path)
        else:
            return f'No User Found'
    else:
        return redirect('/login')

@users_controller.route('/user/edit-profile/@<path:user_id>')
def edit_profile(user_id):
    if 'user_id' in session:
        if session['user_id'] == int(user_id):
            path = get_path()
            user = get_user(all=True)
            return render_template('edit-profile.html', user = user, path=path)
        else:
            return redirect('/logout')
    else:
        return redirect('/login')
    
@users_controller.route('/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id')
    return redirect('/login')