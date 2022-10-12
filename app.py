from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
#protocol+adoptor://user:password@localIPaddress:port/name_of_database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:password123@127.0.0.1:5432/trello'

db = SQLAlchemy(app)

class Card(db.Model):  # Inherit db.Model..
    __tablename__ = 'cards'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))  # String is varchar 100 is length limit
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    status = db.Column(db.String)
    priority = db.Column(db.String)

#Define a custom CLI (terminal) command
@app.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@app.cli.command('seed')
def seed_db():
    card = Card(
        title = 'Start the project',
        description = 'Stage 1 - Creating the database',
        status = 'To Do',
        priority = 'High',
        date = date.today()
    )

    db.session.add(card)
    db.session.commit()
    print('Tables seeded')

@app.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")


@app.route('/')
def index():
    return "Hello World!"

fff