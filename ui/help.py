"""
===============================================================================
CipherMed Secure Medical Information Encryption System

Module Name : help.py

Purpose:
    Displays the user guide for CipherMed.

Responsibilities:
    • Explain login.
    • Explain encryption.
    • Explain decryption.
    • Explain exporting.
    • Explain history.

Author:
    TAIWO OLAMIDE AKINBOBOLA
===============================================================================
"""

import customtkinter as ctk

from modules import theme
class HelpWindow(ctk.CTkToplevel):

    """
    CipherMed Help Window.
    """

    def __init__(self):

        super().__init__()

        self.title("CipherMed Help Centre")

        self.geometry("900x700")
        try:
            self.iconbitmap("assets/icon.ico")
        except Exception:
            pass

        self.resizable(False,False)

        self.configure(

            fg_color=theme.BACKGROUND

        )
        self.title_label = ctk.CTkLabel(

        self,

        text="CipherMed User Guide",

        font=("Segoe UI",24,"bold")

)

        self.title_label.pack(

        pady=(20,15)

)
        self.help_box = ctk.CTkTextbox(

        self,

        width=820,

        height=560

)

        self.help_box.pack(

        padx=20,

        pady=10

)
        guide = """
WELCOME TO CIPHERMED

CipherMed is a desktop application designed to demonstrate how classical
cryptographic techniques can be used to protect confidential patient
medical information.

────────────────────────────────────────────

LOGIN

1. Enter your Staff Username.

2. Enter your Password.

3. Select your Department.

4. Click LOGIN.

If authentication succeeds, the CipherMed Dashboard opens.

────────────────────────────────────────────

PATIENT INFORMATION

The dashboard loads the medical record of:

Sarah Lim Wei Yin

Patient ID:
CM-2400158

Users may edit the medical record before performing encryption.

────────────────────────────────────────────

ENCRYPTION

1. Select a cipher.

Available algorithms:

• Caesar Cipher

• Additive Cipher

• Vigenère Cipher

2. Enter an encryption key.

3. Click Encrypt.

The encrypted medical information appears in the result panel.

────────────────────────────────────────────

DECRYPTION

Click Decrypt to restore the encrypted information back to its original
medical record.

────────────────────────────────────────────

SAVE RECORD

Click Save Record to store encrypted medical information inside the
CipherMed Records folder.

────────────────────────────────────────────

EXPORT

Encrypted records may be exported as

• TXT

• PDF

────────────────────────────────────────────

COPY RESULT

Copies encrypted information directly to the clipboard.

────────────────────────────────────────────

HISTORY

Every encryption and decryption operation is automatically recorded,
including

• Staff member

• Patient

• Cipher

• Key

• Timestamp

────────────────────────────────────────────

EXIT

Click Exit to close CipherMed safely.
"""
        self.help_box.insert(

        "1.0",

        guide

)

        self.help_box.configure(

        state="disabled"

)
        self.close_button = ctk.CTkButton(

        self,

        text="Close",

        width=150,

        command=self.destroy

)

        self.close_button.pack(

        pady=15

)