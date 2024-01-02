from models.base.model_base import mysql

def get_user(of_user):
    cursor = mysql.connection.cursor()
    cursor.execute("""select first_name, last_name, username, user_id, email, bio from reg_user where user_id = '{}'""".format(of_user))
    user = cursor.fetchall()
    return user

def validate_user_db(name, password):
    cursor = mysql.connection.cursor()
    cursor.execute("""SELECT * FROM `reg_user` WHERE `username` LIKE '{}' AND `password` LIKE '{}'""".format(name, password))
    user = cursor.fetchall()
    return user
    
def add_user(first_name, last_name, username,email,password):
    cursor = mysql.connection.cursor()
    cursor.execute("""INSERT INTO `reg_user` (`first_name`, `last_name`, `username`, `email`, `password`, `user_type`) values ("{}","{}","{}","{}","{}","{}")""".format(first_name, last_name, username,email,password, 0))
    mysql.connection.commit()
    
def update_user(first_name, last_name, email,bio, user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("""UPDATE `reg_user` SET first_name = '{}', last_name = '{}', email = '{}', bio = '{}' where user_id = '{}' """.format(first_name, last_name, email,bio, user_id))
    mysql.connection.commit()