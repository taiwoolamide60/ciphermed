"""
===============================================================================
CipherMed Utility Functions

Purpose:
    Reusable helper functions.

===============================================================================
"""

from datetime import datetime


class Utilities:

    @staticmethod
    def current_date():

        return datetime.now().strftime("%d %B %Y")

    @staticmethod
    def current_time():

        return datetime.now().strftime("%I:%M:%S %p")