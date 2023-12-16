from flask import Flask,render_template, request, session, redirect
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL
import os
import string
import random
import datetime
 
app = Flask(__name__)
app.secret_key=os.urandom(24)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'takoloka'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hungerger'
mysql = MySQL(app)

app.config['UPLOAD_FOLDER'] = './static/uploads/'


def get_user(of_user = '', all=False):
    cursor = mysql.connection.cursor()
    if of_user != '':
        cursor.execute("""select first_name, last_name, username, user_id, avatar from reg_user where user_id = '{}'""".format(of_user))
    elif all:
        cursor.execute("""select first_name, last_name, username, user_id, avatar, email from reg_user where user_id = '{}'""".format(session['user_id']))
    else:
        cursor.execute("""select first_name, last_name, username, user_id, avatar from reg_user where user_id = '{}'""".format(session['user_id']))
    user = cursor.fetchall()
    return user

def get_recipes(of_user = ''):
    cursor = mysql.connection.cursor()
    if of_user != '':
       cursor.execute("""select rec_name, recipes.rec_id, description, image, creation_date from recipes INNER JOIN (select user_id, username as user_name from reg_user) as user_details on recipes.creator_id = user_details.user_id where recipes.creator_id = '{}' order by recipes.rec_id desc""".format(of_user))
    else:
       cursor.execute("""select rec_name, recipes.rec_id, description, image, creation_date from recipes INNER JOIN (select user_id, username as user_name from reg_user) as user_details on recipes.creator_id = user_details.user_id order by recipes.rec_id desc""")
    recipes = cursor.fetchall()
    return recipes

def get_path():
    path = request.root_url.replace('/?','')
    return path

@app.route('/')
def home():
    if 'user_id' in session:
        recipes = get_recipes()
        path = get_path()
        user = get_user()
        print(recipes)
        print(path)
        print(user)
        return render_template('index.html', recipes=recipes, user=user, path=path)
    else:
        return redirect('/login')

@app.route('/create-recipe')
def compose():
    if 'user_id' in session:
        path = get_path()
        user = get_user()
        x = datetime.datetime.now()
        date = x.strftime("%B %d, %Y")
        cursor = mysql.connection.cursor()
        cursor.execute("""select ing_id, ing_name, description, price from ingredients""")
        ingredients = cursor.fetchall()
        return render_template('create-recipe.html', user=user, date=date, path=path, ingredients=ingredients)
    else:
        return redirect('/login')

@app.route('/login')
def login():
    if 'user_id' in session:
        return redirect('/')
    else:
        print(request.root_url)
        return render_template('login.html')

@app.route('/register')
def register():
    if 'user_id' in session:
        return redirect('/')
    else:
        return render_template('register.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    name = request.form.get('name')
    password = request.form.get('password')
    cursor = mysql.connection.cursor()
    cursor.execute("""SELECT * FROM `reg_user` WHERE `username` LIKE '{}' AND `password` LIKE '{}'""".format(name, password))
    reg_user = cursor.fetchall()
    if len(reg_user)>0:
        session['user_id'] = reg_user[0][3]
        return redirect('/')
    else:
        return redirect('/login')

@app.route('/add_user', methods=['POST'])
def add_user():
    name=request.form.get('name')
    email=request.form.get('email')
    password=request.form.get('password')
    cursor = mysql.connection.cursor()
    cursor.execute("""INSERT INTO `reg_user` (`first_name`, `last_name`, `username`, `email`, `password`) values ("{}","{}","{}","{}","{}")""".format(name,email,password))
    print("""INSERT INTO `reg_user` (`first_name`, `last_name`, `username`, `email`, `password`) values ("{}","{}","{}","{}","{}")""".format(name,email,password))
    mysql.connection.commit()
    return redirect('/login')

@app.route('/create-recipe', methods=['POST'])
def create_recipe():
    if 'user_id' in session:
        name=request.form.get('name')
        description=request.form.get('description')
        # TODO: Insert INTO recipes_ingredients
        ingredients=request.form.getlist('ingredients')
        print(ingredients)

        user_id = session['user_id']
        x = datetime.datetime.now()
        created_at = x.strftime("%B %d, %Y")
        f = request.files['image']
        cursor = mysql.connection.cursor()
        if f.filename is not '':
            filename = os.path.join(app.config['UPLOAD_FOLDER'], session['user_id'] + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))+secure_filename(f.filename))
            f.save(filename)
            print("""INSERT INTO `recipes` (`rec_name`, `description`, `image`, `creator_id`, `creation_date`) values ("{}","{}","{}","{}","{}")""".format(name, description, filename, user_id, created_at))
            cursor.execute("""INSERT INTO `recipes` (`rec_name`, `description`, `image`, `creator_id`, `creation_date`) values ("{}","{}","{}","{}","{}")""".format(name, description, filename, user_id, created_at))
        else:
            print("""INSERT INTO `recipes` (`rec_name`, `description`, `creator_id`, `creation_date`) values ("{}","{}","{}","{}")""".format(name, description, user_id, created_at))
            cursor.execute("""INSERT INTO `recipes` (`rec_name`, `description`, `creator_id`, `creation_date`) values ("{}","{}","{}","{}")""".format(name, description, user_id, created_at))
        
        cursor_created_recipe = mysql.connection.cursor()
        created_recipe = cursor_created_recipe.execute("""select rec_id from recipes where rec_name = '{}'""".format(name))
        cursor_ingredient = mysql.connection.cursor()
        for ingredient in ingredients:
            print("------ Ingredient: "+ingredient+" ------")
            cursor_ingredient.execute("""INSERT INTO `recipes_ingredients` (`rec_id`, `ingredient_id`) values ("{}","{}")""".format(created_recipe, ingredient))
        mysql.connection.commit()
        return redirect('/')
    else:
        return render_template('login.html')
    
@app.route('/edit-recipe/@<path:rec_id>')
def edit_recipe_page(rec_id):
    if 'user_id' in session:
        path = get_path()
        user = get_user()
        x = datetime.datetime.now()
        date = x.strftime("%B %d, %Y")
        cursor = mysql.connection.cursor()
        cursor.execute("""select ingredient_id, ing_name, description, price from ingredients""")
        ingredients = cursor.fetchall()
        cursor = mysql.connection.cursor()
        cursor.execute("""select rec_id, rec_name, description, image from recipes where rec_id={}""".format(rec_id))
        recipe = cursor.fetchall()
        cursor = mysql.connection.cursor()
        cursor.execute("""select ri_id, rec_id, ing_id from recipes_ingredients where rec_id = {} """.format(rec_id))
        recipe_ingredients = cursor.fetchall()
        return render_template('edit-recipe.html', user=user, date=date, path=path, ingredients=ingredients, recipe=recipe, recipe_ingredients=recipe_ingredients, rec_id=rec_id)
    else:
        return redirect('/login')
    
@app.route('/edit-recipe', methods=['POST'])
def edit_recipe():
    if 'user_id' in session:
        rec_id=request.form.get('rec_id')
        name=request.form.get('name')
        description=request.form.get('description')
        # TODO: Insert INTO recipes_ingredients
        ingredients=request.form.getlist('ingredients')
        print(ingredients)

        user_id = session['user_id']
        x = datetime.datetime.now()
        created_at = x.strftime("%B %d, %Y")
        f = request.files['image']
        cursor = mysql.connection.cursor()
        if f.filename is not '':
            filename = os.path.join(app.config['UPLOAD_FOLDER'], session['user_id'] + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))+secure_filename(f.filename))
            f.save(filename)
            print("""UPDATE `recipes` set `rec_name`="{}", `description`="{}", `creator_id`="{}", `creation_date`="{}" where rec_id={}""".format(name, description, user_id, created_at, rec_id))
            cursor.execute("""UPDATE `recipes` set `rec_name`="{}", `description`="{}", `creator_id`="{}", `creation_date`="{}" where rec_id={}""".format(name, description, user_id, created_at, rec_id))
        else:
            print("""UPDATE `recipes` set `rec_name`="{}", `description`="{}", `creator_id`="{}", `creation_date`="{}" where rec_id={}""".format(name, description, user_id, created_at, rec_id))
            cursor.execute("""UPDATE `recipes` set `rec_name`="{}", `description`="{}", `creator_id`="{}", `creation_date`="{}" where rec_id={}""".format(name, description, user_id, created_at, rec_id))
        
        cursor_created_recipe = mysql.connection.cursor()
        created_recipe = cursor_created_recipe.execute("""select rec_id from recipes where rec_name = '{}'""".format(name))
        cursor_ingredient = mysql.connection.cursor()
        for ingredient in ingredients:
            print("------ Ingredient: "+ingredient+" ------")
            cursor_ingredient.execute("""INSERT INTO `recipes_ingredients` (`rec_id`, `ing_id`) values ("{}","{}")""".format(created_recipe, ingredient))
        mysql.connection.commit()
        return redirect('/')
    else:
        return render_template('login.html')

@app.route('/update-profile', methods=['POST'])
def update_profile():
    if 'user_id' in session:
        username=request.form.get('username')
        email=request.form.get('email')
        user_id = session['user_id']
        cursor = mysql.connection.cursor()
        # print("""INSERT INTO `recipes` (`raw_post`, `user_id`, `posted_at`) values ("{}","{}","{}")""".format(post_data, user_id, created_at))
        cursor.execute("""UPDATE `reg_user` SET username = '{}', email = '{}' where user_id = '{}' """.format(username, email, user_id))
        mysql.connection.commit()
        return redirect('/')
    else:
        return redirect('/login')

@app.route('/@<path:user_id>')
def user(user_id):
    if 'user_id' in session:
        path = get_path()
        res = get_user(user_id)
        user = get_user()
        print(res)
        if len(res) > 0:
            recipes = get_recipes(res[0][1])
            return render_template('profile.html', res = res, user = user, recipes = recipes, path=path)
        else:
            return f'No User Found'
    else:
        return redirect('/login')

@app.route('/@<path:user_id>/edit-profile')
def edit_profile(user_id):
    if 'user_id' in session:
        if session['user_id'] == user_id:
            path = get_path()
            user = get_user(all=True)
            return render_template('edit-profile.html', user = user, path=path)
        else:
            red = '/@'+user_id
            return redirect(red)
    else:
        return redirect('/login')



@app.route('/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id')
    return redirect('/login')

@app.route('/test')
def test():
    return render_template('test.html')


app.run(port=5000, debug=True)