from cartoes.database import db

class Card(db.Model):
    __tablename__ = "card"
    id = db.Column("id", db.Integer, primary_key=True)
    number = db.Column("number", db.String(30), index=True, nullable=False)
    ccv = db.Column("ccv", db.String(5), index=True, nullable=False)
    situation = db.Column("situation", db.String(30), index=True, nullable=False)
    