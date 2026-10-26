"""
===============================================================================
CipherMed Secure Medical Information Encryption System

Module Name : history_window.py

Purpose:
    Displays the encryption and decryption history.

Responsibilities:
    • View encryption history.
    • Refresh records.
    • Clear history.
    • Close history window.

Author:
    TAIWO OLAMIDE AKINBOBOLA

===============================================================================
"""

import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox

from modules.history import HistoryManager
from modules import theme
class HistoryWindow(ctk.CTkToplevel):

    """
    Displays CipherMed Audit History.
    """

    def __init__(self):

        super().__init__()

        self.title("CipherMed Encryption History")

        self.geometry("1100x650")
        try:
            self.iconbitmap("assets/icon.ico")
        except Exception:
            pass

        self.resizable(False, False)

        self.configure(fg_color=theme.BACKGROUND)

        self.history = HistoryManager()

        self.create_widgets()

        self.load_history()
    def create_widgets(self):
        self.title_label = ctk.CTkLabel(

        self,

        text="CipherMed Encryption & Decryption History",

        font=("Segoe UI",22,"bold")

)

        self.title_label.pack(

        pady=(20,15)

)
        columns = (

        "Username",

        "Patient",

        "Patient ID",

        "Cipher",

        "Key",

        "Action",

        "Timestamp"

)

        self.table = ttk.Treeview(

        self,

        columns=columns,

        show="headings",

        height=18

)
        for column in columns:

         self.table.heading(

        column,

        text=column

    )

        self.table.column(

        column,

        width=140,

        anchor="center"

    )
        self.table.pack(

        padx=20,

        pady=15,

        fill="both",

        expand=True

)
        self.button_frame = ctk.CTkFrame(

        self,

        fg_color="transparent"

)

        self.button_frame.pack(

        pady=15

)
        self.refresh_button = ctk.CTkButton(

        self.button_frame,

        text="Refresh",

        width=140,

        command=self.load_history

)

        self.refresh_button.grid(

        row=0,

        column=0,

        padx=10

)
        self.clear_button = ctk.CTkButton(

        self.button_frame,

        text="Clear History",

        width=140,

        fg_color="#C62828",

        command=self.clear_history

)

        self.clear_button.grid(

        row=0,

        column=1,

        padx=10

)
        self.close_button = ctk.CTkButton(

        self.button_frame,

        text="Close",

        width=140,

        command=self.destroy

)

        self.close_button.grid(

        row=0,

        column=2,

        padx=10

)
    def load_history(self):

        for item in self.table.get_children():

         self.table.delete(item)

        records = self.history.get_history()

        for record in records:

         self.table.insert(

            "",

            "end",

            values=record

        )
    def clear_history(self):

        answer = messagebox.askyesno(

        "Confirm",

        "Delete all encryption history?"

    )

        if answer:

         self.history.clear_history()

        self.load_history()