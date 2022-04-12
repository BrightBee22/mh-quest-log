from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class HunterForm(FlaskForm):
    name = StringField ('Hunter Name', validators=[DataRequired(), Length(min=1, max=16)])
    rank = IntegerField ('Hunter Rank', validators=[DataRequired(), NumberRange(min=1, max=999)])
    weapon = StringField ('Weapon Used', validators=[DataRequired(), Length(max=16)])
    monster = StringField ('Monster Name', validators=[DataRequired(), Length(max=40)])
    submit = SubmitField('Add Hunter Details')

