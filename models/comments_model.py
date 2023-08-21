from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'InterestNook.mwb'

class Comments:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def add_comment(cls, data):
        query = 'INSERT INTO comments (content) VALUE (%(content)s);'
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def delete_comment(cls, data):
        query = 'DELETE FROM comments where id = %(id)s;'
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_comment(cls, data):
        query = 'SELECT * FROM comments WHERE id = %(id)s;'
        results = connectToMySQL(db).query_db(query, data)
        return results

    @staticmethod
    def validate_comment(form_data):
        is_valid = True

        if len(form_data['content']) < 1:
            flash("Comment must be more than 1 character long")
            is_valid = False
        return is_valid