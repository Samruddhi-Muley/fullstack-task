from flask import Blueprint, render_template, request, redirect
from models import projects, contacts, subscribers

public_bp = Blueprint("public", __name__)

@public_bp.route("/")
def home():
    try:
        all_projects = list(
            projects.find()
            .sort("_id", -1)
            .limit(20)
        )
    except Exception as e:
        print("Mongo error:", e)
        all_projects = []

    return render_template("index.html", projects=all_projects)


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
    subscribers.insert_one({
        "email": request.form["email"]
    })
    return redirect("/")
