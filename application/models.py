from application import db 

class Tasks(db.Model):
    lid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())