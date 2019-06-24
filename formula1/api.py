import functools
import json

from flask import (
    Blueprint, flash, g, request, url_for
)

from driver.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

"""def currentrace():
        db = get_db()
        error = None
        db.execute('SELECT * FROM DRIVESEASON').fetchall()
    
    return """
