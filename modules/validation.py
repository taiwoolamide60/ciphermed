"""
===============================================================================
CipherMed Validation Module

Purpose:
    Validates user input.

===============================================================================
"""


class Validation:
    """
    Contains reusable validation functions.
    """

    @staticmethod
    def validate_login_input(username, password, department):
        """
        Validates login fields.

        Returns
        -------
        tuple(bool,str)
        """

        if username.strip() == "":
            return False, "Please enter your username."

        if password.strip() == "":
            return False, "Please enter your password."

        if department.strip() == "":
            return False, "Please select a department."

        return True, ""