from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, current_user
from .models import User

views = Blueprint('views', __name__)

@views.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        email = request.form["email"]
        passw = request.form["password"]
        if email == "" or passw == "":
            message = "All fields are required !!"
            return render_template("login.html", message=message)
        
        exi_user = User.query.filter_by(mail=email).first()
        if exi_user:
            if passw == exi_user.password:
                return redirect("/home")
            else:
                message = "Invalid Password"
                return render_template("login.html", message=message)
        else:
            message = "Address not listed"
            return render_template("login.html", message=message)
    return render_template("login.html")
