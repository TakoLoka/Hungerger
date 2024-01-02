from flask import render_template, request, session, redirect

from models.base.model_base import app
from models.users import *
from models.recipes import *
from models.ingredients import *

from controllers.users_controller import users_controller
from controllers.recipes_controller import recipes_controller

app.register_blueprint(users_controller)
app.register_blueprint(recipes_controller)

def get_path():
    path = request.root_url.replace('/?','')
    return path

@app.route('/')
def home():
    if 'user_id' in session:
        recipes = get_recipes()
        path = get_path()
        user = get_user(session['user_id'])
        print(user)
        return render_template('index.html', recipes=recipes, user=user, path=path)
    else:
        return redirect('/login')

@app.route('/test')
def test():
    return render_template('test.html')


app.run(port=5000, debug=True)