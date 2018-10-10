from app import db

class Verse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), index=True)
    linjeforening = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '{}'.format(self.text)