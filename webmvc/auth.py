from webmvc import db
from flask import Blueprint, render_template, flash, request, redirect, url_for
from .models import User
from flask_login import login_required, login_user, current_user

auth = Blueprint('auth', __name__)

@auth.route("/index", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        nom = request.form["surname"]
        prenom = request.form["first_name"]
        email = request.form["email"]
        passe = request.form["password"]
        conf_pass = request.form["confirm_password"]
        
        new_user = User(nom=nom, prenom=prenom, mail=email, password=passe)
        exi_user = User.query.filter_by(mail=email).first()
        
        if not all([nom, prenom, email, passe, conf_pass]):
            message = "All fields must be filled in!!"
            return render_template("index.html", message=message)
        elif (conf_pass != passe):
            message = "Passwords could not be confirmed please try again"
            return render_template("index.html", message=message)
        elif exi_user:
            message = "This account already exists make sure you identify yourself or change email"
            return render_template("index.html", message=message)
        else:
            try:
                db.session.add(new_user)
                db.session.commit()
                return redirect("/")
            except Exception:
                message = "We were unable to register for you"
                return render_template("index.html", message=message)
    return render_template("index.html")

@auth.route("/home/")
def home():
    users = User.query.all()
    return render_template("home.html", exi_user=current_user, users=users)

@auth.route("/about")
def about():
    return render_template("about.html")

@auth.route("/logout")
@login_required
def logout():
    return redirect("/")

