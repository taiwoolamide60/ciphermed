"""
===============================================================================
CipherMed Authentication Module

Purpose:
    Handles staff authentication.

Author:
    TAIWO OLAMIDE AKINBOBOLA
===============================================================================
"""

from modules.database import DatabaseManager


class Authentication:
    """
    Handles login authentication.
    """

    def __init__(self):

        self.database = DatabaseManager()

    def login(self, username, password, department):
        """
        Authenticates a user.

        Parameters
        ----------
        username : str
        password : str
        department : str

        Returns
        -------
        tuple | None
        """

        return self.database.validate_login(
            username,
            password,
            department
        )