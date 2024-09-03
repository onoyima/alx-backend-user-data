#!/usr/bin/env python3
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

