from flask import render_template, redirect, url_for
from application import app, db
from application.models import Tasks
from application.form import TaskForm

# Route that points to a url. 
# HTTP REQUESTS GET, POST, PUT, DELETE 
# Example of change
@app.route("/")
def hello_world(): 
    # Code exists inside of the functions 
    return render_template('home.html', title="Homepage")

@app.route("/about", methods = ['GET', 'POST'])
def about(): 
    return "Hello this is the about page."

#GETS data from database and displays: 

@app.route("/list", methods=['GET'])
def list_item():
    items = Tasks.query.all()
    return render_template('name.html', items=items)

@app.route("/additem", methods=['POST', 'GET'])
def additem():
    form = TaskForm()
    if form.validate_on_submit():
        items = Tasks(
            name = form.name.data
        )
        db.session.add(items)
        db.session.commit()
        return redirect(url_for('list_item'))
    return render_template('add.html', form=form)
