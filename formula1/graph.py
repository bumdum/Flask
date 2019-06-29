import functools
import json

from flask import (
    Blueprint, flash, g, jsonify, request, render_template, url_for
)

from formula1.db import get_db

bp = Blueprint('graph', __name__)

@bp.route('/')
def races():
    db = get_db()
    races = db.execute('SELECT raceId, name FROM races WHERE [year] = 2017').fetchall()
    g.races = [dict(zip(tuple ('rn') ,i)) for i in races]
    return render_template('races.html')


@bp.route('/teams')
def teams():
    db = get_db()
    error = None
    results = db.execute('SELECT * FROM results WHERE raceId = ? ORDER BY rank', (18,)).fetchall()
    return render_template('teams.html')