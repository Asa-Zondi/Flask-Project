from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    return render_template("home.html", user=current_user)

#@views.route('/reports')
#@login_required
#def reports():
#    return render_template("reports.html", user=current_user)