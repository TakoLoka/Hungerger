import datetime
from flask import Blueprint, render_template, request, session, redirect


recipes_controller = Blueprint('recipes_controller', __name__,
                        template_folder='../views', static_folder="../static")

from models.users import *
from models.recipes import *
from models.ingredients import *

def get_path():
    path = request.root_url.replace('/?','')
    return path
    
def column(matrix, i):
    return [row[i] for row in matrix]

@recipes_controller.route('/create-recipe')
def compose():
    if 'user_id' in session:
        path = get_path()
        user = get_user(session['user_id'])
        x = datetime.datetime.now()
        date = x.strftime('%Y-%m-%d %H:%M:%S')
        ingredients = get_ingredients()
        return render_template('create-recipe.html', user=user, date=date, path=path, ingredients=ingredients)
    else:
        return redirect('/login')

@recipes_controller.route('/create-recipe', methods=['POST'])
def create_recipe():
    if 'user_id' in session:
        name=request.form.get('name')
        description=request.form.get('description')
        # TODO: Insert INTO recipes_ingredients
        ingredients=request.form.getlist('ingredients')
        print(ingredients)
        user_id = session['user_id']
        x = datetime.datetime.now()
        created_at = x.strftime('%Y-%m-%d %H:%M:%S')
        insert_recipe(name, description, user_id, created_at, ingredients)
        return redirect('/')
    else:
        return render_template('login.html')
    
@recipes_controller.route('/edit-recipe/@<path:rec_id>')
def edit_recipe_page(rec_id):
    if 'user_id' in session:
        path = get_path()
        user = get_user(session['user_id'])
        x = datetime.datetime.now()
        date = x.strftime('%Y-%m-%d %H:%M:%S')
        ingredients = get_ingredients()
        recipe = get_recipes_for_edit(rec_id)
        recipe_ingredients = get_recipe_ingredients(rec_id)
        recipe_ingredients = column(recipe_ingredients, 1)
        return render_template('edit-recipe.html', user=user, date=date, path=path, ingredients=ingredients, recipe=recipe, recipe_ingredients=recipe_ingredients, rec_id=rec_id)
    else:
        return redirect('/login')
    
@recipes_controller.route('/edit-recipe', methods=['POST'])
def edit_recipe():
    if 'user_id' in session:
        rec_id=request.form.get('rec_id')
        name=request.form.get('name')
        description=request.form.get('description')
        ingredients=request.form.getlist('ingredients')
        print(ingredients)
        user_id = session['user_id']
        x = datetime.datetime.now()
        created_at = x.strftime('%Y-%m-%d %H:%M:%S')
        edit_recipe(name, description, user_id, created_at, rec_id, ingredients)
        return redirect('/')
    else:
        return render_template('login.html')
    
@recipes_controller.route('/delete-recipe/@<path:rec_id>')
def delete_recipe(rec_id):
    if 'user_id' in session:
        delete_recipe_db(rec_id)
        return redirect('/')
    else:
        return render_template('login.html')

@recipes_controller.route('/recipe-details/@<path:rec_id>')
def recipe_details(rec_id):
    if 'user_id' in session:
        path = get_path()
        user = get_user(session['user_id'])
        x = datetime.datetime.now()
        date = x.strftime('%Y-%m-%d %H:%M:%S')
        ingredients = get_ingredients()
        recipe = get_recipes_for_edit(rec_id)
        recipe_ingredients = get_recipe_ingredients(rec_id)
        return render_template('recipe-details.html', user=user, date=date, path=path, ingredients=ingredients, recipe=recipe, recipe_ingredients=recipe_ingredients, rec_id=rec_id)
    else:
        return redirect('/login')