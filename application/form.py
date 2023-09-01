from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField

from application.models import Tasks

class TaskForm(FlaskForm):
    name = StringField("Tasks")
    submit = SubmitField("Submit")