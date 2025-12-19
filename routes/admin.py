from flask import Blueprint, render_template, request, redirect
from models import projects, clients, contacts, subscribers

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/")
def dashboard():
    return render_template("admin/dashboard.html")

@admin_bp.route("/projects", methods=["GET", "POST"])
def manage_projects():
    if request.method == "POST":
        projects.insert_one({
            "name": request.form["name"],
            "description": request.form["description"],
            "image": request.form["image"]
        })
        return redirect("/admin/projects")
    return render_template("admin/projects.html", projects=projects.find())

@admin_bp.route("/clients", methods=["GET", "POST"])
def manage_clients():
    if request.method == "POST":
        clients.insert_one({
            "name": request.form["name"],
            "designation": request.form["designation"],
            "description": request.form["description"],
            "image": request.form["image"]
        })
        return redirect("/admin/clients")
    return render_template("admin/clients.html", clients=clients.find())

@admin_bp.route("/contacts")
def view_contacts():
    return render_template("admin/contacts.html", contacts=contacts.find())

@admin_bp.route("/subscribers")
def view_subscribers():
    return render_template("admin/subscribers.html", subs=subscribers.find())
