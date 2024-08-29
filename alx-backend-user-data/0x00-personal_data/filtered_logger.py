#!/usr/bin/env python3
"""
Module for a filtered logger
"""
import re
import logging
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')

class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the message to redact sensitive information
        """
        message = super(RedactingFormatter, self).format(record)
        return self.redact(message)

    def redact(self, message: str) -> str:
        """
        Redact sensitive information in the log message
        """
        for field in self.fields:
            message = re.sub(f"{field}=[^;]+", f"{field}={self.REDACTION}", message)
        return message
