from application import app, db
from flask import render_template, request, redirect, url_for
from application.forms import HunterForm
from application.models import Hunter, QuestLog

@app.route('/')
def home():
    all_hunters = Hunter.query.all()
    return render_template('homepage.html', all_hunters=all_hunters)

@app.route('/addhunter', methods=['GET', 'POST'])
def addhunter():
    form = HunterForm()


    if request.method == "POST":
        hunters = Hunter(name=form.name.data, rank=form.rank.data, email=form.email.data)

        db.session.add(hunters)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('addhunter.html', form=form)
