#!/usr/bin/env python3
"""
Module for password encryption
"""
import bcrypt

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """
    Verify a hashed password against the provided password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
