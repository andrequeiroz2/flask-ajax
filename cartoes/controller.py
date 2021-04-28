from cartoes.model import Card
from cartoes.database import db

def create_card(number, ccv, situation):
    card = Card(number=number, ccv=ccv, situation=situation)
    db.session.add(card)
    db.session.commit()

def list_all_card():
    cards = Card.query.all()
    return cards

def list_card_id(id):
    card = Card.query.filter_by(id=id).first()
    return card

