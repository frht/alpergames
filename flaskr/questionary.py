from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort



bp = Blueprint('questionary', __name__, url_prefix='/questionary')

@bp.route('/q1')
def q1():
    return render_template('questionary/q1.html')

@bp.route('/q2')
def q2():
    return render_template('questionary/q2.html')

