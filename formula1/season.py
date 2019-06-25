import functools
import json

from flask import (
    Blueprint, flash, g, request, render_template, url_for
)

from formula1.db import get_db

bp = Blueprint('season', __name__, url_prefix='/season')

@bp.route('/')
def season():
    return render_template('season/races.html')