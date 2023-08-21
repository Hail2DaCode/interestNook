from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.comments_model import Comments

@app.route("INSERT ROUTE HERE")
def comment_form(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template('comment.html')

@app.route("INSERT ROUTE HERE")
def submit_comment(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    data = {
        'post_id': id,
        'user_id': session['user_id'],
        'content' : request.form['content'],
    }
    Comments.add_comment(data)
    return redirect('INSERT ROUTE HERE')