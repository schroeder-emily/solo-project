from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db_name = 'soloproject'

class Workout:
    db_name = 'soloproject'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.title = db_data['title']
        self.description = db_data['description']
        self.duration = db_data['duration']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO workouts (title, description, duration, user_id) VALUES (%(title)s,%(description)s,%(duration)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM workouts;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_workouts = []
        for row in results:
            print(row['title'])
            all_workouts.append( cls(row) )
        return all_workouts
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM workouts WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE workouts SET title=%(title)s, description=%(description)s, duration=%(duration)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM workouts WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_workout(workout):
        is_valid = True
        query = "SELECT * FROM workouts WHERE title = %(title)s;"
        results = connectToMySQL(db_name).query_db(query,workout)
        if len(workout['title']) <= 0:
            is_valid = False
            flash("Title must be greater than 0","workout")
        if workout['description'] == "":
            is_valid = False
            flash("Please enter a description","workout")
        if len(workout['duration']) <= 0:
            is_valid = False
            flash("Duration must be greater than 0","car")
        
        
        return is_valid
