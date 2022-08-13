from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False)


# db.create_all()
# item1 = Item(name="Iphone 10", price=500, barcode="893212299897", description="DESCUENTOS--S")
# db.session.add(item1)
# db.session.commit()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/market')
def market():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)


@app.route('/about/<username>')
def about_user(username):
    return f"<h1> hola {username}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
