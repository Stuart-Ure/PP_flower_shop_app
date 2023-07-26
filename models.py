from app import db

class Flower(db.Model):
    # __tablename__ = "flower"

    id = db.Column(db.Integer, primary_key = True)
    # Primary key will auto increment ID
    flower_name = db.Column(db.String(64))
    flower_price = db.Column(db.Integer)
    order = db.relationship('Order', backref='flower') 
    # backref creates on the task a user property, so you can do task.user a back reference

    def __repr__(self):
        return f'<flower {self.id}: {self.flower_name} {self.flower_price} {self.order}>'

class Order(db.Model):
    # __tablename__ = "order"

    id = db.Column(db.Integer, primary_key = True)
    # Primary key will auto increment ID
    order = db.Column(db.String(64))
    order_qty = db.Column(db.Integer)
    order_date = db.Column(db.String(64))
    flower_id = db.Column(db.Integer, db.ForeignKey("flower.id"))
    # backref creates on the task a user property, so you can do task.user a back reference

    def __repr__(self):
        return f'<order {self.id}: {self.order} {self.order_qty} {self.order_date} {self.flower_id}>'


