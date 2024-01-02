from models.base.model_base import mysql

def get_recipes():
    cursor = mysql.connection.cursor()
    cursor.execute("""select rec_name, recipes.rec_id, description, image, creation_date, user_details.user_id from recipes INNER JOIN (select user_id, username as user_name from reg_user) as user_details on recipes.creator_id = user_details.user_id order by recipes.rec_id desc""")
    recipes = cursor.fetchall()
    return recipes

def insert_recipe(name, description, user_id, created_at, ingredients):
    cursor = mysql.connection.cursor()
    cursor.execute("""INSERT INTO `recipes` (`rec_name`, `description`, `creator_id`, `creation_date`, `dietary_type`) values ("{}","{}","{}","{}","{}")""".format(name, description, user_id, created_at, "None"))
    mysql.connection.commit()
    cursor_created_recipe = mysql.connection.cursor()
    cursor_created_recipe.execute("""select rec_id, rec_name from recipes where rec_name = '{}'""".format(name))
    created_recipe_id = cursor_created_recipe.fetchall()
    cursor_ingredient = mysql.connection.cursor()
    for ingredient in ingredients:
        print("------ Ingredient: "+ingredient+" ------")
        cursor_ingredient.execute("""INSERT INTO `recipes_ingredients` (`rec_id`, `ing_id`) values ("{}","{}")""".format(created_recipe_id[0][0], ingredient))
    mysql.connection.commit()
    
def get_recipes_for_edit(rec_id):
    cursor = mysql.connection.cursor()
    cursor.execute("""select rec_name, description, image from recipes where rec_id={}""".format(rec_id))
    recipe = cursor.fetchall()
    return recipe

def edit_recipe(name, description, user_id, created_at, rec_id, ingredients):
    cursor = mysql.connection.cursor()
    cursor.execute("""UPDATE `recipes` set `rec_name`="{}", `description`="{}", `creator_id`="{}", `creation_date`="{}" where rec_id={}""".format(name, description, user_id, created_at, rec_id))
    cursor_ingredient = mysql.connection.cursor()
    cursor_ingredient.execute("""DELETE FROM `recipes_ingredients` where rec_id={}""".format(rec_id))
    for ingredient in ingredients:
        print("------ Ingredient: "+ingredient+" ------")
        cursor_ingredient.execute("""INSERT INTO `recipes_ingredients` (`rec_id`, `ing_id`) values ("{}","{}")""".format(rec_id, ingredient))
    mysql.connection.commit()
    
def delete_recipe_db(rec_id):
    cursor = mysql.connection.cursor()
    cursor.execute("""DELETE FROM `recipes` where rec_id={}""".format(rec_id))
    cursor_ingredient = mysql.connection.cursor()
    cursor_ingredient.execute("""DELETE FROM `recipes_ingredients` where rec_id={}""".format(rec_id))
    cursor.execute("""DELETE FROM `recipes_ingredients` where rec_id={}""".format(rec_id))
    mysql.connection.commit()