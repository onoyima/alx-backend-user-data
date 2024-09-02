#!/usr/bin/env python3
import os
import stat
import subprocess

# List of dependencies
dependencies = [
    "flask",
    "flask-cors"
]

directories = [
    "api/v1", 
    "api/v1/auth", 
    "api/v1/views"
]

files_content = {
    "README.md": "# ALX Backend User Data\n\nThis project contains basic authentication for a simple API.",
    
    "api/v1/app.py": '''#!/usr/bin/env python3
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
''',

    "api/v1/views/index.py": '''#!/usr/bin/env python3
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
''',

    "api/v1/auth/__init__.py": '''#!/usr/bin/env python3
"""
Auth package initializer
"""
''',

    "api/v1/auth/auth.py": '''#!/usr/bin/env python3
"""
Auth module
"""
from typing import List, TypeVar
from flask import request

class Auth:
    """Auth class to manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determine if a path requires authentication"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        for ep in excluded_paths:
            if ep[-1] != '/':
                ep += '/'
            if path == ep:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns the authorization header"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user"""
        return None
'''
}

def create_structure():
    """Create directories and files with content"""
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    for file, content in files_content.items():
        with open(file, 'w') as f:
            f.write(content + '\n')  # Ensure each file ends with a newline
        os.chmod(file, stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)  # Make the file executable

def install_dependencies():
    """Install required Python dependencies"""
    print("Installing dependencies...")
    subprocess.check_call([os.sys.executable, "-m", "pip", "install"] + dependencies)

if __name__ == "__main__":
    create_structure()
    install_dependencies()
    print("Project structure and dependencies setup successfully.")

