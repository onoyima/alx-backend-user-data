#!/usr/bin/env python3
"""
Index module
"""
from flask import Blueprint, jsonify, abort

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

@app_views.route('/status', methods=['GET'])
def status():
    """Returns status"""
    return jsonify({"status": "OK"})

@app_views.route('/unauthorized', methods=['GET'])
def unauthorized():
    """Raises 401 error"""
    abort(401)

@app_views.route('/forbidden', methods=['GET'])
def forbidden():
    """Raises 403 error"""
    abort(403)

