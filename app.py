from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://user@localhost:5432/flower_shop"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Flower, Order