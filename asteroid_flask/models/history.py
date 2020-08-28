from asteroid_flask.services.database import db

class History(db.Document):
    song = db.StringField()
    duration = db.IntField()
    artist = db.StringField()
    album = db.StringField()
    file = db.StringField()
    url = db.StringField()
