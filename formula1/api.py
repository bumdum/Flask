import functools
import json

from flask import (
    Blueprint, flash, g, jsonify, request, url_for
)

from formula1.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/get_toplaps', methods=["GET"])
def get_toplaps():
    raceId = request.args.get('a', 0, type=int)
    db = get_db()
    #d.forename || " " || d.surname AS name
    results = db.execute('SELECT d.surname AS name, l.time FROM lapTimes AS l JOIN drivers AS d ON l.driverId = d.driverId WHERE l.raceId = ? ORDER BY l.position, l.time, l.milliseconds LIMIT 5', (raceId,)).fetchall()
    return jsonify([dict(zip(tuple ('nt') ,i)) for i in results])