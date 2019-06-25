import functools
import json

from flask import (
    Blueprint, flash, g, request, render_template, url_for
)

from formula1.db import get_db

bp = Blueprint('graph', __name__, url_prefix='/graph')

@bp.route('/')
def races():
    return render_template('graph/races.html')


@bp.route('/teams')
def teams():
    db = get_db()
    error = None
    results = db.execute('SELECT TOP(5) * FROM results WHERE raceId = ? ORDER BY rank', (raceId,)).fetchall()
    return render_template('graph/teams.html')