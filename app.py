from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Home
from schemas import HomeSchema
from extensions import db

url = "postgres://postgres:postgres@localhost:5432/homes"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
migrate = Migrate(app, db)

from models import Home
@app.route("/homes")
def home():
    query = Home.query

    min_sell_price = request.args.get("min_sell_price")
    max_sell_price = request.args.get("max_sell_price")

    if min_sell_price is not None:
        query = query.filter(Home.sell_price >= min_sell_price)
    if max_sell_price is not None:
        query = query.filter(Home.sell_price >= max_sell_price)

    results = query.all()
    json_homes = HomeSchema(many=True).dump(results)

    return jsonify(json_homes)

app.run(debug=True)