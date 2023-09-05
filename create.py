from application import db, app
from application.models import Tasks

#Making a change
with app.app_context():
    db.drop_all()
    db.create_all()

    item1 = Tasks(lid = 1, name = "Teach Flask")
    item2 = Tasks(lid = 2, name = "Teach Github")

    db.session.add(item1)
    db.session.add(item2)
    db.session.commit()
