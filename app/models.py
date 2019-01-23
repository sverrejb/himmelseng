from app import db

class VerseEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), index=True)
    linjeforening = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '{}'.format(self.text)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}