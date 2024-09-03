#!/usr/bin/env python3
"""
Main app module
"""
from flask import Flask, jsonify, abort
from api.v1.views.index import app_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "*"}})

auth = None

@app.before_request
def before_request():
    """Handle filtering of each request"""
    if auth:
        if not auth.require_auth(request.path, ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']):
            return
        if not auth.authorization_header(request):
            abort(401)
        if not auth.current_user(request):
            abort(403)

@app.errorhandler(401)
def unauthorized(error):
    """Unauthorized handler"""
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error):
    """Forbidden handler"""
    return jsonify({"error": "Forbidden"}), 403

if __name__ == "__main__":
    host = os.getenv('API_HOST', '0.0.0.0')
    port = os.getenv('API_PORT', 5000)
    app.run(host=host, port=int(port))

