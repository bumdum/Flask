import functools
import json

from flask import (
    Blueprint, flash, g, request, render_template, url_for
)

from formula1.db import get_db

season_bp = Blueprint('season', __name__, url_prefix='/season')

@season_bp.route('/season', methods='GET')
def season():

    return render_template('season/season.html')