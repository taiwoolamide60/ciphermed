"""
===============================================================================
CipherMed Secure Medical Information Encryption System

Module Name : patient_manager.py

Purpose:
    Retrieves patient records from the CipherMed database.

Responsibilities:
    • Load patient information.
    • Search patient by Patient ID.
    • Retrieve all patient records.

Author:
    TAIWO OLAMIDE AKINBOBOLA

===============================================================================
"""

import sqlite3
class PatientManager:

    def __init__(self):

        self.connection = sqlite3.connect("database/ciphermed.db")

        self.cursor = self.connection.cursor()
    def get_patient(self, patient_id):

        self.cursor.execute("""

        SELECT *

        FROM patients

        WHERE patient_id=?

        """,

        (patient_id,)

    )

        return self.cursor.fetchone()
    def get_all_patients(self):

        self.cursor.execute("""

        SELECT *

        FROM patients

        ORDER BY name

        """)

        return self.cursor.fetchall()
    def close(self):

        self.connection.close()