from models.base.model_base import mysql

def get_ingredients():
    cursor = mysql.connection.cursor()
    cursor.execute("""select ing_id, ing_name, description, price from ingredients""")
    return cursor.fetchall()

def get_recipe_ingredients(rec_id):
    cursor = mysql.connection.cursor()
    cursor.execute("""select rec_id, ing_id from recipes_ingredients where rec_id = {} """.format(rec_id))
    return cursor.fetchall()