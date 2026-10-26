"""
===============================================================================
CipherMed Secure Medical Information Encryption System

Module Name : history.py

Purpose:
    Manages encryption and decryption history.

Responsibilities:
    • Record every encryption.
    • Record every decryption.
    • Retrieve history.
    • Clear history.

Author:
    TAIWO OLAMIDE AKINBOBOLA
===============================================================================
"""

import sqlite3
from datetime import datetime
class HistoryManager:

    """
    Stores CipherMed audit history.
    """

    def __init__(self):

        self.connection = sqlite3.connect("database/ciphermed.db")

        self.cursor = self.connection.cursor()

        self.create_table()
    def create_table(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        patient_id TEXT,

        patient_name TEXT,

        cipher TEXT,

        encryption_key TEXT,

        action TEXT,

        timestamp TEXT

    )

    """)

        self.connection.commit()
    def save_history(

        self,

        username,

        patient_id,

        patient_name,

        cipher,

        key,

        action

):

        current_time = datetime.now().strftime(

        "%d/%m/%Y %H:%M:%S"

    )

        self.cursor.execute("""

        INSERT INTO history(

        username,

        patient_id,

        patient_name,

        cipher,

        encryption_key,

        action,

        timestamp

    )

    VALUES(?,?,?,?,?,?,?)

    """,

    (

        username,

        patient_id,

        patient_name,

        cipher,

        key,

        action,

        current_time

    ))

        self.connection.commit()
    def get_history(self):

        self.cursor.execute("""

    SELECT

    username,

    patient_name,

    patient_id,

    cipher,

    encryption_key,

    action,

    timestamp

    FROM history

    ORDER BY id DESC

    """)

        return self.cursor.fetchall()
    def clear_history(self):

        self.cursor.execute(

        "DELETE FROM history"

    )

        self.connection.commit()
    def close(self):

        self.connection.close()