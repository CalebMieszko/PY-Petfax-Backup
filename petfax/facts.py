from flask import Blueprint, render_template

# fact submission page

bp = Blueprint('facts', __name__, url_prefix='/facts')


@bp.route('/new')
def index():
    return render_template('facts/new.html')
