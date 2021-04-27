from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from cartoes.model import Card
from cartoes.database import db


class CardForm(FlaskForm):
    number = StringField('Number', validators=[InputRequired(), Length(min=5, max=30, message=('Min 5 and Max 30 digits'))])
    ccv = StringField('CCV', validators=[InputRequired(), Length(min=2, max=5, message=('Min 3 and Max 5 digits'))])
    situation = StringField("Situation", validators=[InputRequired(), Length(max=30, message=('Max 30 digits'))])
    submit = SubmitField('OK')

    def validate_number(self, number):
        card = Card.query.filter_by(number=number.data).first()
        if card is not None:
            raise ValidationError('Card already registered.')