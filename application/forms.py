from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class HunterForm(FlaskForm):
    name = StringField ('Hunter Name', validators=[DataRequired(), Length(min=1, max=16)])
    rank = IntegerField ('Hunter Rank', validators=[DataRequired(), NumberRange(min=1, max=999)])
    submit = SubmitField('Add Hunter Details')