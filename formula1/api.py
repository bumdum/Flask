import functools
import json

from flask import (
    Blueprint, flash, g, request, url_for
)

from formula1.db import get_db

api_bp = Blueprint('api', __name__, url_prefix='/api')

@app.route('/get_race')
def get_races():
    raceId = request.args.get('a', 0, type=int)
    db = get_db()
    error = None
    results = db.execute('SELECT TOP(5) * FROM results WHERE raceId = ? ORDER BY rank', (raceId,)).fetchall()
    return jsonify(results)
