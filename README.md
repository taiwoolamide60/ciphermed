# CipherMed Secure Medical Information Encryption System

## Description

CipherMed is a Python desktop application developed to demonstrate the application of classical cryptographic algorithms to confidential patient medical information within a simulated healthcare environment.

Designed for CipherCare Medical Centre, the application allows authorised staff to authenticate, manage patient records, encrypt and decrypt medical information, review activity history, and export records in TXT and PDF formats.

The system demonstrates how encryption can be incorporated into a desktop-based medical information management application to support confidentiality and controlled access to patient information.

## Features

- **Staff Authentication** — Login validation using designated staff accounts.
- **SQLite Database** — Stores staff accounts, patient records, and encryption/decryption history.
- **Patient Record Management** — Displays and manages fictional patient medical information.
- **Caesar Cipher** — Encrypts and decrypts text using a character-shift technique.
- **Additive Cipher** — Applies a numerical shift key to encrypt and decrypt text.
- **Vigenère Cipher** — Uses a keyword-based substitution technique for encryption and decryption.
- **Encryption and Decryption** — Supports the selection of a classical cipher and its corresponding key.
- **History Logging** — Records encryption and decryption activities.
- **TXT Export** — Exports medical information into text files.
- **PDF Export** — Generates PDF documents containing medical information.
- **Graphical User Interface** — Provides a desktop interface built with CustomTkinter.

## Technologies

- Python 3
- CustomTkinter
- SQLite
- ReportLab
- PyInstaller (for Windows executable packaging)

## Demo Login Credentials

Use one of the following demonstration accounts to access CipherMed.

| Username     | Password    | Department     |
|     ---      |      ---    |      ---       |
| `admin`      | `admin123`  | Administration |
| `doctor01`   | `doctor123` | Respiratory    |
| `nurse01`    | `nurse123`  | Nursing        |
| `pharmacist` | `pharma123` | Pharmacy       |

**Important:** Select the department that corresponds to the chosen account on the login screen. The username, password, and department must match the account configured in the application.

These accounts are intended for demonstration purposes within the fictional healthcare environment used by CipherMed.

## Running the System from Source

### Prerequisites

- Python 3 installed on your computer.
- The CipherMed project files.
- A terminal such as PowerShell or Command Prompt.

### Installation

**1. Download or clone the repository**

Download the project files from GitHub and open a terminal in the project directory.

**2. Install the required dependencies**

Run the following command:

```bash
pip install -r requirements.txt
```

**3. Launch CipherMed**

Run the application using:

```bash
python main.py
```

**4. Log in**

Enter one of the demonstration accounts listed in the Demo Login Credentials section, including its matching department.

## Running the Windows Executable

A standalone Windows executable can be generated using PyInstaller.

After a successful build, the executable will be located at:

```text
dist/CipherMed.exe
```

Double-click `CipherMed.exe` to launch the application.

The executable should be tested before distribution to verify that the database, application resources, authentication, encryption/decryption functions, and export features work correctly.

If a prebuilt executable is published, it can be made available through the repository's **GitHub Releases** section.

## Database

CipherMed uses SQLite to manage its application data.

The database contains tables for:

- **Staff** — Stores staff usernames, password hashes, names, and departments.
- **Patients** — Stores fictional patient information, including patient IDs, diagnoses, medications, and allergies.
- **History** — Stores encryption/decryption activity information, including the selected cipher, key, action, and timestamp.

The database is initialised by the application, which inserts default demonstration accounts and sample patient records when the corresponding tables are empty.

## Project Purpose

CipherMed was developed as an educational software project to demonstrate the integration of classical cryptographic algorithms into a desktop medical information management system.

The project combines authentication, database management, encryption/decryption, activity logging, and document export within a simulated healthcare setting.

## Security Disclaimer

CipherMed is an educational demonstration, not a production healthcare system.

The Caesar, Additive, and Vigenère ciphers are classical cryptographic techniques and are **not suitable for protecting real medical records or other sensitive information**. The demonstration login credentials are also not intended for production use.

The application uses SHA-256 hashing for its demonstration staff passwords. Production authentication should use a dedicated password-hashing algorithm such as Argon2id, bcrypt, or scrypt, alongside appropriate access controls and secure key management.

All sample patient records should remain fictional. Do not use real patient information or publish confidential data in the repository.

## Author

**Taiwo Olamide Akinbobola**
