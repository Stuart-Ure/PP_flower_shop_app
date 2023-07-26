from flask import Flask, render_template, redirect, Blueprint, request
from app import db
from models import Flower, Order

flower_blueprint = Blueprint("flowers", __name__)

@flower_blueprint.route("/")
def flower_homepage():
    flower=Flower.query.all()
    return render_template("/index.jinja", title="Welcome To The Flower System", flower=flower)

@flower_blueprint.route("/flower")
def flower():
    flowers=Flower.query.all()
    print("FLOWERS")
    print(flower)
    return render_template("/index.jinja", title="All Flowers", flowers=flowers)

@flower_blueprint.route("/orders")
def orders():
    orders=Order.query.all()
    return render_template("/order.jinja", title="All Orders", orders=orders)

@flower_blueprint.route("/flower_edit")
def flower_edit():
    return render_template("/flower_edit.jinja", title="Edit Flower")

@flower_blueprint.route("/flower_add_form")
def flower_add_form():
    return render_template("/flower_add.jinja", title="Add A Flower")

@flower_blueprint.route("/flower_add", methods=["POST"])
def flower_add():
    flower_name = request.form ['flower_name']
    flower_price = request.form ['price']

    flower = Flower(flower_name = flower_name, flower_price = flower_price)

    db.session.add(flower)
    db.session.commit()

    return render_template("/flower_add.jinja", title="Add A Flower")

@flower_blueprint.route("/order_add_form")
def order_add_form():
    return render_template("/order_add.jinja", title="Add An Order")

@flower_blueprint.route("/order_add", methods=["POST"])
def order_add():
    order = request.form ['order_name']
    order_qty = request.form ['order_qty']
    flower_id = request.form ['flower_id']
    order_date = request.form ['date']

    order = Order(order = order, order_qty = order_qty, order_date = order_date, flower_id = flower_id)

    db.session.add(order)
    db.session.commit()

    # return render_template("/order_add.jinja", title="Add An Order")
    return redirect('/orders')