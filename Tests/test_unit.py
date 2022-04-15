from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from application import app, db
from application.models import Hunter, Questlog
from flask import url_for

class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        return app

    def setUp(self):
        db.create_all()
        hunter1 = Hunter(name="Fighter", rank="111")
        hunter2 = Hunter(name="Archer", rank="222")
        quest1 = Questlog (monster="King Kong", weapon="sword", hunter=hunter1)
        quest2 = Questlog(monster="Godzilla", weapon="spear", hunter=hunter2)
        db.session.add(hunter1)
        db.session.add(hunter2)
        db.session.add(quest1)
        db.session.add(quest2)
        db.session.commit


    def tearDown(self):
        db.drop_all()

class TestViewQuest(TestBase):
    def test_view_page(self):
        response = self.client.get(url_for('addhunter'))
        self.assertEqual(response.status_code, 200)

    
class TestDelete(TestBase):  
    def delete_hunt(self):
        response = self.client.delete(url_for('delete_hunt'),
        data = dict(name="Fighter", rank = "111"))
        assert len(Hunter.query.all()) == 1

class TestUpdate(TestBase):
    def update_hunt(self):
        response = self.client.update(url_for('complete_hunt'))
        self.assertEqual(response.status_code, 200)
    
class TestAddQuest(TestBase):
    def test_new_hunt(self):
        response=self.client.post(url_for('addhunter'),
        data = dict(name="Assasin", rank ="333", weapon="dagger", monster="dracula"),
        follow_redirects=True)
        self.assertEqual(response.status_code, 200)



