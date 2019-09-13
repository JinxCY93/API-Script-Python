from extensions import db

class Home(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    Sell = db.Column(db.Integer)
    List = db.Column(db.Integer)
    Living = db.Column(db.Integer)
    Rooms = db.Column(db.Integer)
    Beds = db.Column(db.Integer)
    Baths = db.Column(db.Integer)
    Age = db.Column(db.Integer)
    Acres = db.Column(db.Float)
    Taxes = db.Column(db.Integer)


# class tempHome(db.Model):
#     Sell = db.Column(db.Integer)
#     List = db.Column(db.Integer)
#     Living = db.Column(db.Integer)
#     Rooms = db.Column(db.Integer)
#     Beds = db.Column(db.Integer)
#     Baths = db.Column(db.Integer)
#     Age = db.Column(db.Integer)
#     Acres = db.Column(db.Float)
#     Taxes = db.Column(db.Integer)