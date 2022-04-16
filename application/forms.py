from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange

class HunterForm(FlaskForm):
    name = StringField ('Hunter Name', validators=[DataRequired(), Length(min=1, max=16)])
    rank = IntegerField ('Hunter Rank', validators=[DataRequired(), NumberRange(min=1, max=999)])
    weapon = SelectField ('Weapon Used', choices=[
        ("Sword and Shield", "Sword and Shield"),
        ("Great Sword", "Great Sword"),
        ("Long Sword", "Long Sword"),
        ("Dual Blades", "Dual Blades"),
        ("Lance", "Lance"),
        ("Gunlance", "Gunlance"),
        ("Hammer", "Hammer"),
        ("Hunting Horn", "Hunting Horn"),
        ("Switch Axe", "Switch Axe"),
        ("Charge Blade", "Charge Blade"),
        ("Insect Glaive", "Insect Glaive"),
        ("Bow", "Bow"),
        ("Light Bowgun", "Light Bowgun"),
        ("Heavy Bowgun", "Heavy Bowgun")

    ])
    monster = StringField ('Monster Name', validators=[DataRequired(), Length(max=40)])
    submit = SubmitField('Add Hunter Details')

