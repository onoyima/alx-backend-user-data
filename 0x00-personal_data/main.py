#!/usr/bin/env python3
"""
Main file for testing the filtered logger
"""
import logging
from filtered_logger import RedactingFormatter, PII_FIELDS

def get_logger() -> logging.Logger:
    """
    Creates a logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)

    return logger

if __name__ == "__main__":
    logger = get_logger()
    logger.info("name=John Doe; email=john.doe@example.com; phone=123-456-7890; ssn=123-45-6789; password=secret")
