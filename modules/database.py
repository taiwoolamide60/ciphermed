"""
==============================================================================
CipherMed Secure Medical Information Encryption System

Module Name : database.py

Purpose:
    Creates and manages the SQLite database used by CipherMed.

Responsibilities:
    • Create all required database tables.
    • Insert default staff accounts.
    • Insert sample patient records.
    • Store encryption/decryption history.
    • Provide reusable database functions.

Author:
    TAIWO OLAMIDE AKINBOBOLA

==============================================================================
"""

# =============================================================================
# Import Required Libraries
# =============================================================================

import sqlite3
import hashlib
from pathlib import Path

# =============================================================================
# Database Location
# =============================================================================

DATABASE_FOLDER = Path("database")
DATABASE_FOLDER.mkdir(exist_ok=True)

DATABASE_PATH = DATABASE_FOLDER / "ciphermed.db"

# =============================================================================
# Password Security Functions
# =============================================================================

def hash_password(password):
    """
    Converts a plaintext password into a SHA-256 hash.

    Parameters:
        password (str): User password.

    Returns:
        str: SHA-256 hashed password.
    """

    return hashlib.sha256(password.encode()).hexdigest()

# =============================================================================
# Database Manager Class
# =============================================================================


class DatabaseManager:
    """
    Handles all database operations for CipherMed.
    """

    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.connection.cursor()

        self.create_tables()
        self.insert_default_staff()
        self.insert_default_patients()
        # -------------------------------------------------------------------------
    # Create Staff Table
    # -------------------------------------------------------------------------

    def create_tables(self):
        """
        Creates all required database tables.
        """

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS staff(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE,

            password TEXT,

            full_name TEXT,

            department TEXT

        )
        """)
        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS patients(

            patient_id TEXT PRIMARY KEY,

            name TEXT,

            age INTEGER,

            gender TEXT,

            blood_group TEXT,

            doctor TEXT,

            ward TEXT,

            diagnosis TEXT,

            medication TEXT,

            allergy TEXT

        )

        """)
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
        # -------------------------------------------------------------------------
    # Insert Default Staff Accounts
    # -------------------------------------------------------------------------

    def insert_default_staff(self):
        """
        Inserts default staff accounts only if the table is empty.
        """

        self.cursor.execute("SELECT COUNT(*) FROM staff")

        if self.cursor.fetchone()[0] > 0:
            return

        staff_accounts = [

    (
        "admin",
        hash_password("admin123"),
        "Dr. Amir Hassan",
        "Administration"
    ),

    (
        "doctor01",
        hash_password("doctor123"),
        "Dr. Michael Tan",
        "Respiratory"
    ),

    (
        "nurse01",
        hash_password("nurse123"),
        "Sarah Johnson",
        "Nursing"
    ),

    (
        "pharmacist",
        hash_password("pharma123"),
        "Emily Wong",
        "Pharmacy"
    )

]

        self.cursor.executemany("""

        INSERT INTO staff
        (username,password,full_name,department)

        VALUES(?,?,?,?)

        """, staff_accounts)

        self.connection.commit()
        # -------------------------------------------------------------------------
    # Insert Sample Patient Records
    # -------------------------------------------------------------------------

    def insert_default_patients(self):
        """
        Inserts fictional patient records for demonstration purposes.
        """

        self.cursor.execute("SELECT COUNT(*) FROM patients")

        if self.cursor.fetchone()[0] > 0:
            return

        patients = [

            (
                "CCMC-2026-0158",
                "Sarah Lim Wei Yin",
                31,
                "Female",
                "A+",
                "Dr. Amir Hassan",
                "Respiratory Ward B",
                "Acute Bronchitis",
                "Amoxicillin 500 mg   \nTake one capsule three times daily.",
                "Penicillin"
            ),

            (
                "CCMC-2026-0182",
                "Michael Tan Wei Jian",
                44,
                "Male",
                "B+",
                "Dr. Emily Lim",
                "Cardiology Ward A",
                "Hypertension",
                "Amlodipine",
                "None"
            ),

            (
                "CCMC-2026-0224",
                "Aisha Nur Syafiqah",
                26,
                "Female",
                "O+",
                "Dr. Amir Hassan",
                "Ward A",
                "Asthma",
                "Salbutamol Inhaler",
                "Dust"
            ),

            (
                "CCMC-2026-0268",
                "David Wong Kai Ren",
                53,
                "Male",
                "AB+",
                "Dr. Michael Tan",
                "Orthopaedics",
                "Fractured Tibia",
                "Ibuprofen 400 mg",
                "None"
            ),

            (
                "CCMC-2026-0317",
                "Emily Tan Jia Xin",
                37,
                "Female",
                "O-",
                "Dr. Amir Hassan",
                "Neurology",
                "Migraine",
                "Sumatriptan",
                "Latex"
            ),

]

        self.cursor.executemany("""

        INSERT INTO patients

        VALUES(?,?,?,?,?,?,?,?,?,?)

        """, patients)

        self.connection.commit()
        # -------------------------------------------------------------------------
    # Validate Login
    # -------------------------------------------------------------------------

    def validate_login(self, username, password, department):
        """
        Validates the entered login credentials.

        Returns:
            User information if authentication succeeds.
            None if authentication fails.
        """

        self.cursor.execute("""
        
        SELECT *

        FROM staff

        WHERE username = ?

        AND password = ?

        AND department = ?

        """,
        (
            username,
            hash_password(password),
            department
        ))

        return self.cursor.fetchone()
    
    # -------------------------------------------------------------------------
    # Retrieve All Patient Names
    # -------------------------------------------------------------------------

    def get_patient_names(self):
        """
        Returns all patient names for the Patient Record selector.
        """

        self.cursor.execute("""

        SELECT name

        FROM patients

        ORDER BY name

        """)

        return [row[0] for row in self.cursor.fetchall()]

    # -------------------------------------------------------------------------
    # Close Database Connection
    # -------------------------------------------------------------------------

    def close(self):
        """
        Closes the SQLite database connection.
        """

        self.connection.close()