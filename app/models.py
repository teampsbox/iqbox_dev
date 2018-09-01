from datetime import datetime
from app import db


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True, nullable=False)
    body = db.Column(db.String(250), index=True, nullable=False)
    by = db.Column(db.String(25), index=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Quote Title:{}, Body:{}, by:{}, posted on:{}>'.format(self.title, self.body, self.by, self.timestamp)
