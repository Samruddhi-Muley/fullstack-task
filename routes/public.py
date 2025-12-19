from flask import Blueprint, render_template, request, redirect
from models import projects, clients, contacts, subscribers

public_bp = Blueprint("public", __name__)

@public_bp.route("/")
def home():
    return render_template(
        "public/index.html",
        projects=list(projects.find()),
        clients=list(clients.find())
    )

@public_bp.route("/contact", methods=["POST"])
def contact():
    contacts.insert_one({
        "name": request.form["name"],
        "email": request.form["email"],
        "mobile": request.form["mobile"],
        "city": request.form["city"]
    })
    return redirect("/")

@public_bp.route("/subscribe", methods=["POST"])
def subscribe():
    subscribers.insert_one({"email": request.form["email"]})
    return redirect("/")
