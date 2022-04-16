from application import app, db
from flask import render_template, request, redirect, url_for
from application.forms import HunterForm
from application.models import Hunter, Questlog

@app.route('/')
def home():
    form = HunterForm()
    all_hunters = Hunter.query.all()
    all_quests = Questlog.query.all()
    return render_template('homepage.html', all_hunters=all_hunters, all_quests=all_quests)


@app.route('/addhunter', methods=['GET', 'POST'])
def addhunter():
    form = HunterForm()
    
    if request.method == "POST":

        hunters = Hunter(name=form.name.data, rank=form.rank.data)

        db.session.add(hunters)

        quests = Questlog(weapon=form.weapon.data, monster=form.monster.data, hunter=hunters)

        db.session.add(quests)

        db.session.commit()

        return redirect(url_for('home'))

    return render_template('addhunter.html', form=form)

@app.route('/complete/<completed>/<int:id>')
def complete_hunt(completed, id):
    quest = Questlog.query.get(id)
    if completed == 'True':
        quest.completed = True
        db.session.commit()
    elif completed == 'False':
        quest.completed = False
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete_hunt(id):
    quest = Questlog.query.get(id)
    hunter = Hunter.query.get(id)
    db.session.delete(quest)
    db.session.delete(hunter)
    db.session.commit()
    return redirect(url_for('home'))
