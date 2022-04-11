from application import db
from datetime import datetime

class Hunter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    quests = db.relationship ('QuestLog', backref ='hunter')

class QuestLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weapon = db.Column(db.String(16), nullable=False)
    monster = db.Column(db.String(40), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    completed = db.Column(db.Boolean, nullable=False, default=False)
    hunter_id = db.Column(db.Integer, db.ForeignKey('hunter.id'), nullable=False)

