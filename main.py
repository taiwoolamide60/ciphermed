"""
===============================================================================
CipherMed Secure Medical Information Encryption System

Main Application Entry Point

Author : TAIWO OLAMIDE AKINBOBOLA
Version: 1.0
===============================================================================
"""

from modules.database import DatabaseManager
from ui.splash import SplashScreen


def main():
    """
    Starts the CipherMed application.
    """

    # Create the database if it does not already exist.
    DatabaseManager()

    # Launch the splash screen.
    app = SplashScreen()
    app.mainloop()


if __name__ == "__main__":
    main()