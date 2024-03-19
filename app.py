from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.secret_key = '1F7VkTpXpSBo9P60skv9Kq$23QwD9FG44U'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
db = SQLAlchemy(app)


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(20), nullable=False)


class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    store = db.Column(db.String(20), nullable=False)
    art = db.Column(db.Integer, nullable=False)
    operation = db.Column(db.String(20), nullable=False)
    count = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)


class Product(db.Model):
    art = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    count = db.Column(db.Integer, nullable=False)
    provider = db.Column(db.String(20), nullable=False)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/store_list")
def store_list():
    s = []
    for i in Store.query.all():
        print(i.id, i.area)
        s.append([i.id, i.area])
    return str(s)


@app.route("/trade_list")
def trade_list():
    s = []
    for i in Trade.query.all():
        print(i.id, i.date, i.store, i.art, i.operation, i.count, i.price)
        s.append([i.id, i.date, i.store, i.art, i.operation, i.count, i.price])
    return str(s)


@app.route("/product_list")
def product_list():
    s = []
    for i in Product.query.all():
        print(i.art, i.department, i.name, i.unit, i.count, i.provider)
        s.append([i.art, i.department, i.name, i.unit, i.count, i.provider])
    return str(s)


if __name__ == '__main__':
    app.run()
