"""
===============================================================================
CipherMed Secure Medical Information Encryption System

Module Name : about.py

Purpose:
    Displays information about CipherMed.

Responsibilities:
    • Display system information.
    • Display project purpose.
    • Display implemented ciphers.
    • Display developer information.
    • Display software version.

Author:
    TAIWO OLAMIDE AKINBOBOLA

===============================================================================
"""

import customtkinter as ctk

from modules import theme
class AboutWindow(ctk.CTkToplevel):

    """
    CipherMed About Window.
    """

    def __init__(self):

        super().__init__()

        self.title("About CipherMed")

        self.geometry("850x650")
        try:
            self.iconbitmap("assets/icon.ico")
        except Exception:
            pass

        self.resizable(False, False)

        self.configure(
            fg_color=theme.BACKGROUND
        )
        self.logo = ctk.CTkLabel(

        self,

        text="🛡",

        font=("Segoe UI Emoji",60)

)

        self.logo.pack(
        pady=(20,10)
)
        self.system_name = ctk.CTkLabel(

        self,

        text="CipherMed Secure Medical Information Encryption System",

        font=("Segoe UI",22,"bold")

)

        self.system_name.pack()
        self.version = ctk.CTkLabel(

        self,

        text="Version 1.0",

        font=("Segoe UI",14)

)

        self.version.pack(
        pady=(5,20)
)
        self.information = ctk.CTkTextbox(

        self,

        width=760,

        height=360

)

        self.information.pack(
        padx=20,
        pady=10
)
        about_text = """
SYSTEM OVERVIEW

CipherMed is a secure desktop application developed to demonstrate the
application of classical cryptographic algorithms in protecting
confidential patient medical information.

The application authenticates authorised healthcare staff before allowing
access to sensitive medical records.

IMPLEMENTED FEATURES

• Secure Staff Login

• Patient Information Management

• Caesar Cipher

• Additive Cipher

• Vigenère Cipher

• Encryption

• Decryption

• Clipboard Support

• Record Saving

• TXT Export

• PDF Export

• Encryption History

• Digital Clock

• Current Date

• Professional Graphical User Interface

SOFTWARE ARCHITECTURE

The application follows a modular software architecture.

Major modules include:

• Authentication

• Database

• Encryption Engine

• History Manager

• File Manager

• Dashboard

• Help Centre

PROJECT PURPOSE

The objective of CipherMed is to demonstrate how cryptography can improve
the confidentiality of electronic medical information while providing an
easy-to-use graphical interface suitable for healthcare professionals.

DEVELOPER

TAIWO OLAMIDE AKINBOBOLA

Copyright © 2026
"""
        self.information.insert(

        "1.0",

        about_text

)

        self.information.configure(
        state="disabled"
)
        self.close_button = ctk.CTkButton(

        self,

        text="Close",

        width=160,

        command=self.destroy

)

        self.close_button.pack(
        pady=20
)