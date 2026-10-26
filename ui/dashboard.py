
"""
===============================================================================
CipherMed Secure Medical Information Encryption System

Module Name:
    dashboard.py

Purpose:
    Displays the CipherMed dashboard after successful staff login.

Author:
    TAIWO OLAMIDE AKINBOBOLA
===============================================================================
"""

import customtkinter as ctk
import pyperclip

from datetime import datetime
from tkinter import messagebox

from modules import theme
from modules.encryption_engine import EncryptionEngine
from modules.file_manager import FileManager
from modules.history import HistoryManager
from modules.patient_manager import PatientManager

from ui.help import HelpWindow
from ui.about import AboutWindow
from ui.history_window import HistoryWindow


class Dashboard(ctk.CTk):

    def __init__(self, staff):

        super().__init__()

        self.staff = staff

        self.encryption_engine = EncryptionEngine()
        self.file_manager = FileManager()
        self.history = HistoryManager()
        self.patient_manager = PatientManager()

        self.title("CipherMed Secure Medical Information Encryption System")
        self.geometry("1450x890")

        try:
            self.iconbitmap("assets/icon.ico")
        except Exception:
            pass

        self.resizable(False, False)
        self.configure(fg_color=theme.BACKGROUND)

        # ==========================================================
        # Main Container
        # ==========================================================

        self.main_frame = ctk.CTkFrame(
            self,
            fg_color=theme.BACKGROUND
        )

        self.main_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        # ==========================================================
        # Header
        # ==========================================================

        self.header = ctk.CTkFrame(
            self.main_frame,
            height=80,
            fg_color=theme.HEADER,
            corner_radius=12
        )

        self.header.pack(fill="x")
        self.header.pack_propagate(False)

        self.logo = ctk.CTkLabel(
            self.header,
            text="🛡 CipherMed",
            font=("Segoe UI", 28, "bold"),
            text_color="white"
        )

        self.logo.pack(
            side="left",
            padx=25
        )

        self.date_label = ctk.CTkLabel(
            self.header,
            text="",
            font=("Segoe UI", 14),
            text_color="white"
        )

        self.date_label.pack(
            side="right",
            padx=20
        )

        self.clock_label = ctk.CTkLabel(
            self.header,
            text="",
            font=("Segoe UI", 18, "bold"),
            text_color="white"
        )

        self.clock_label.pack(
            side="right",
            padx=20
        )

        self.update_clock()

        # ==========================================================
        # Body
        # ==========================================================

        self.body = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )

        self.body.pack(
            fill="both",
            expand=True,
            pady=15
        )

        # ==========================================================
        # Left Panel
        # ==========================================================

        self.left_panel = ctk.CTkFrame(
            self.body,
            width=330,
            fg_color="white",
            corner_radius=12
        )

        self.left_panel.pack(
            side="left",
            fill="y",
            padx=(0, 15)
        )

        self.left_panel.pack_propagate(False)

        # ==========================================================
        # Workspace
        # ==========================================================

        self.workspace = ctk.CTkScrollableFrame(
            self.body,
            fg_color="white",
            corner_radius=12
        )

        self.workspace.pack(
            side="right",
            fill="both",
            expand=True
        )

        # ==========================================================
        # Staff Information
        # ==========================================================

        self.staff_card = ctk.CTkFrame(
            self.left_panel,
            fg_color="#F8FAFC",
            corner_radius=12
        )

        self.staff_card.pack(
            fill="x",
            padx=15,
            pady=(20, 10)
        )

        self.staff_title = ctk.CTkLabel(
            self.staff_card,
            text="Staff Information",
            font=("Segoe UI", 18, "bold")
        )

        self.staff_title.pack(pady=(15, 10))

        self.staff_avatar = ctk.CTkLabel(
            self.staff_card,
            text="👨‍⚕️",
            font=("Segoe UI Emoji", 60)
        )

        self.staff_avatar.pack()

        self.staff_name = ctk.CTkLabel(
            self.staff_card,
            text=self.staff[3],
            font=("Segoe UI", 16, "bold")
        )

        self.staff_name.pack(pady=5)

        self.department = ctk.CTkLabel(
            self.staff_card,
            text=self.staff[4],
            font=("Segoe UI", 13)
        )

        self.department.pack()

        self.login_time = ctk.CTkLabel(
            self.staff_card,
            text=f"Login Time: {datetime.now().strftime('%H:%M:%S')}",
            font=("Segoe UI", 12)
        )

        self.login_time.pack(
            pady=(5, 15)
        )

        # ==========================================================
        # Patient Information Card
        # ==========================================================

        self.patient_card = ctk.CTkFrame(
            self.left_panel,
            fg_color="#F8FAFC",
            corner_radius=12
        )

        self.patient_card.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(10, 20)
        )

        self.patient_title = ctk.CTkLabel(
            self.patient_card,
            text="Patient Information",
            font=("Segoe UI", 18, "bold")
        )

        self.patient_title.pack(
            pady=(15, 10)
        )

        self.patient_avatar = ctk.CTkLabel(
            self.patient_card,
            text="👩",
            font=("Segoe UI Emoji", 60)
        )

        self.patient_avatar.pack(
            pady=(0, 5)
        )

        # Updated patient details display:
        # - Explicit height and wrapping prevent vertical clipping.
        # - Label/value formatting is handled by load_patient().
        # - Left alignment and spacing improve readability.

        self.patient_details = ctk.CTkLabel(
            self.patient_card,
            text="Select a patient to view details.",
            justify="left",
            anchor="w",
            font=("Segoe UI", 13),
            height=300,
            wraplength=250
        )

        self.patient_details.pack(
            padx=20,
            pady=(5, 20),
            anchor="w",
            fill="x"
        )

        # ==========================================================
        # Workspace Title
        # ==========================================================

        self.workspace_title = ctk.CTkLabel(
            self.workspace,
            text="Medical Information Encryption Workspace",
            font=("Segoe UI", 20, "bold")
        )

        self.workspace_title.pack(
            pady=(20, 15)
        )

        # ==========================================================
        # Patient Selection
        # ==========================================================

        self.patient_label = ctk.CTkLabel(
            self.workspace,
            text="Select Patient"
        )

        self.patient_label.pack(
            anchor="w",
            padx=30
        )

        patients = self.patient_manager.get_all_patients()
        print(patients)
        self.patient_map = {}

        patient_names = []

        for patient in patients:

            patient_names.append(patient[1])
            self.patient_map[patient[1]] = patient

        self.patient_box = ctk.CTkComboBox(
            self.workspace,
            values=patient_names,
            width=320,
            command=lambda value: self.load_patient()
        )
        self.patient_box.configure(command=self.load_patient)
        self.patient_box.pack(
            anchor="w",
            padx=30,
            pady=(5, 15)
        )

        self.load_button = ctk.CTkButton(
            self.workspace,
            text="📄 Load Patient",
            command=self.load_patient
        )

        self.load_button.pack(
            anchor="w",
            padx=30,
            pady=(0, 15)
        )

        # ==========================================================
        # Encryption Algorithm
        # ==========================================================

        self.cipher_label = ctk.CTkLabel(
            self.workspace,
            text="Encryption Algorithm"
        )

        self.cipher_label.pack(
            anchor="w",
            padx=30
        )

        self.cipher_box = ctk.CTkComboBox(
            self.workspace,
            values=[
                "Caesar Cipher",
                "Additive Cipher",
                "Vigenère Cipher"
            ],
            width=250
        )

        self.cipher_box.pack(
            anchor="w",
            padx=30,
            pady=(5, 15)
        )

        self.cipher_box.set("Caesar Cipher")

        # ==========================================================
        # Encryption Key
        # ==========================================================

        self.key_label = ctk.CTkLabel(
            self.workspace,
            text="Encryption Key"
        )

        self.key_label.pack(
            anchor="w",
            padx=30
        )

        self.key_entry = ctk.CTkEntry(
            self.workspace,
            width=250,
            placeholder_text="Enter key"
        )

        self.key_entry.pack(
            anchor="w",
            padx=30,
            pady=(5, 15)
        )

        # ==========================================================
        # Plain Text
        # ==========================================================

        self.plain_label = ctk.CTkLabel(
            self.workspace,
            text="Plain Medical Information"
        )

        self.plain_label.pack(
            anchor="w",
            padx=30
        )

        self.plain_text = ctk.CTkTextbox(
            self.workspace,
            width=850,
            height=220
        )

        self.plain_text.pack(
            padx=30,
            pady=(5, 15)
        )

        # ==========================================================
        # Result Label
        # ==========================================================

        self.result_label = ctk.CTkLabel(
            self.workspace,
            text="Encrypted / Decrypted Result"
        )

        self.result_label.pack(
            anchor="w",
            padx=30
        )

        # ==========================================================
        # Result Textbox
        # ==========================================================

        self.result_text = ctk.CTkTextbox(
            self.workspace,
            width=850,
            height=220
        )

        self.result_text.pack(
            padx=30,
            pady=(5, 20)
        )

        print(self.workspace.winfo_children())

        # ==========================================================
        # Button Frame
        # ==========================================================

        self.button_frame = ctk.CTkFrame(
            self.workspace,
            fg_color="transparent",
            height=100
        )

        self.button_frame.pack(
            pady=10
        )
        self.button_frame.pack(fill="x")
        print("Button frame packed")

        # ==========================================================
        # Encrypt Button
        # ==========================================================

        self.encrypt_button = ctk.CTkButton(
            self.button_frame,
            text="🔒 Encrypt",
            width=150,
            height=40,
            corner_radius=10,
            fg_color="#0810ED",
            hover_color="#0810ED",
            font=("Segoe UI", 14, "bold"),
            command=self.encrypt_record
        )

        self.encrypt_button.grid(
            row=0,
            column=0,
            padx=5
        )

        # ==========================================================
        # Decrypt Button
        # ==========================================================

        self.decrypt_button = ctk.CTkButton(
            self.button_frame,
            text="🔓 Decrypt",
            width=150,
            height=40,
            corner_radius=10,
            fg_color="#1ADD04",
            hover_color="#1ADD04",
            font=("Segoe UI", 14, "bold"),
            command=self.decrypt_record
        )

        self.decrypt_button.grid(
            row=0,
            column=1,
            padx=5
        )

        # ==========================================================
        # Copy Button
        # ==========================================================

        self.copy_button = ctk.CTkButton(
            self.button_frame,
            text="📋 Copy",
            width=150,
            height=40,
            corner_radius=10,
            fg_color="#9509C4",
            hover_color="#9509C4",
            font=("Segoe UI", 14, "bold"),
            command=self.copy_result
        )

        self.copy_button.grid(
            row=0,
            column=2,
            padx=5
        )

        # ==========================================================
        # Save Button
        # ==========================================================

        self.save_button = ctk.CTkButton(
            self.button_frame,
            text="💾 Save",
            width=150,
            height=40,
            corner_radius=10,
            fg_color="#ED6F08",
            hover_color="#ED6F08",
            font=("Segoe UI", 14, "bold"),
            command=self.save_record
        )

        self.save_button.grid(
            row=0,
            column=3,
            padx=5
        )

        # ==========================================================
        # Export TXT Button
        # ==========================================================

        self.export_txt_button = ctk.CTkButton(
            self.button_frame,
            text="📄 Export TXT",
            width=150,
            height=40,
            corner_radius=10,
            fg_color="#08D6ED",
            hover_color="#08D6ED",
            font=("Segoe UI", 14, "bold"),
            command=self.export_txt
        )

        self.export_txt_button.grid(
            row=0,
            column=4,
            padx=5
        )

        # ==========================================================
        # Export PDF Button
        # ==========================================================

        self.export_pdf_button = ctk.CTkButton(
            self.button_frame,
            text="📕 Export PDF",
            width=150,
            height=40,
            corner_radius=10,
            fg_color="#ED0808",
            hover_color="#ED0808",
            font=("Segoe UI", 14, "bold"),
            command=self.export_pdf
        )

        self.export_pdf_button.grid(
            row=0,
            column=5,
            padx=5
        )

        # ==========================================================
        # History Button
        # ==========================================================

        self.history_button = ctk.CTkButton(
            self.button_frame,
            text="📜 History",
            width=150,
            height=40,
            corner_radius=10,
            fg_color="#A91265",
            hover_color="#A91265",
            font=("Segoe UI", 14, "bold"),
            command=self.open_history
        )

        self.history_button.grid(
            row=1,
            column=1,
            padx=5,
            pady=10
        )

        # ==========================================================
        # Help Button
        # ==========================================================

        self.help_button = ctk.CTkButton(
            self.button_frame,
            text="❓ Help",
            width=150,
            height=40,
            corner_radius=10,
            fg_color="#5E5E60",
            hover_color="#5E5E60",
            font=("Segoe UI", 14, "bold"),
            command=self.open_help
        )

        self.help_button.grid(
            row=1,
            column=2,
            padx=5,
            pady=10
        )

        # ==========================================================
        # About Button
        # ==========================================================

        self.about_button = ctk.CTkButton(
            self.button_frame,
            text="ℹ About",
            width=150,
            height=40,
            corner_radius=10,
            fg_color="#384702",
            hover_color="#384702",
            font=("Segoe UI", 14, "bold"),
            command=self.open_about
        )

        self.about_button.grid(
            row=1,
            column=3,
            padx=5,
            pady=10
        )

        # ==========================================================
        # Exit Button
        # ==========================================================

        self.exit_button = ctk.CTkButton(
            self.button_frame,
            text="🚪 Exit",
            width=150,
            height=40,
            corner_radius=10,
            hover_color="#B81C1C",
            font=("Segoe UI", 14, "bold"),
            fg_color=theme.ERROR,
            command=self.exit_system
        )

        self.exit_button.grid(
            row=1,
            column=4,
            padx=5,
            pady=10
        )

        print("Exit button created")

        if patient_names:
            self.patient_box.set(patient_names[0])
            self.load_patient()

    # ==========================================================
    # Update Clock
    # ==========================================================

    def update_clock(self):

        now = datetime.now()

        self.clock_label.configure(
            text=now.strftime("%H:%M:%S")
        )

        self.date_label.configure(
            text=now.strftime("%A, %d %B %Y")
        )

        self.after(
            1000,
            self.update_clock
        )

    # ==========================================================
    # Load Selected Patient
    # ==========================================================

    def load_patient(self, value=None):

        selected = self.patient_box.get()

        if not selected or selected not in self.patient_map:
            return

        patient = self.patient_map[selected]

        self.patient = patient

        record = (
            f"Patient Name: {patient[1]}\n"
            f"Patient ID: {patient[0]}\n"
            f"Age: {patient[2]} Years\n"
            f"Gender: {patient[3]}\n"
            f"Blood Group: {patient[4]}\n"
            f"Diagnosis: {patient[7]}\n"
            f"Prescription: {patient[8]}\n"
            f"Allergy: {patient[9]}\n"
            f"Attending Doctor: {patient[5]}\n"
            f"Ward: {patient[6]}"
        )

        self.plain_text.delete("1.0", "end")
        self.plain_text.insert("1.0", record)

        # Patient details are displayed without leading indentation or
        # excessive blank lines so every field remains readable.

        patient_information = (
            f"Patient Name:  {patient[1]}\n\n"
            f"Patient ID:  {patient[0]}\n\n"
            f"Age:  {patient[2]} Years\n\n"
            f"Gender:  {patient[3]}\n\n"
            f"Blood Group:  {patient[4]}\n\n"
            f"Diagnosis:  {patient[7]}\n\n"
            f"Attending Doctor:  {patient[5]}\n\n"
            f"Ward:  {patient[6]}"
        )

        self.patient_details.configure(
            text=patient_information,
            height=300,
            wraplength=250
        )

    # ==========================================================
    # Encrypt Record
    # ==========================================================

    def encrypt_record(self):
        print("Encrypt button pressed")

        plaintext = self.plain_text.get(
            "1.0",
            "end"
        ).strip()

        algorithm = self.cipher_box.get()

        key = self.key_entry.get().strip()

        if plaintext == "":
            messagebox.showwarning(
                "Missing Data",
                "No patient information available."
            )
            return

        if key == "":
            messagebox.showwarning(
                "Missing Key",
                "Please enter an encryption key."
            )
            return

        if algorithm in (
            "Caesar Cipher",
            "Additive Cipher"
        ):

            if not key.isdigit():

                messagebox.showerror(
                    "Invalid Key",
                    "Caesar and Additive ciphers require a numeric key."
                )

                return

        if algorithm == "Vigenère Cipher":

            if not key.isalpha():

                messagebox.showerror(
                    "Invalid Key",
                    "Vigenère Cipher requires alphabetic characters only."
                )

                return

        encrypted = self.encryption_engine.encrypt(
            algorithm,
            plaintext,
            key
        )

        self.result_text.delete(
            "1.0",
            "end"
        )

        self.result_text.insert(
            "1.0",
            encrypted
        )

        self.history.save_history(
            self.staff[1],
            self.patient[0],
            self.patient[1],
            algorithm,
            key,
            "Encryption"
        )

        messagebox.showinfo(
            "Success",
            "Medical record encrypted successfully."
        )
        print("History saved")

    # ==========================================================
    # Decrypt Record
    # ==========================================================

    def decrypt_record(self):

        ciphertext = self.result_text.get(
            "1.0",
            "end"
        ).strip()

        algorithm = self.cipher_box.get()

        key = self.key_entry.get().strip()

        if ciphertext == "":
            messagebox.showwarning(
                "Missing Data",
                "There is no encrypted record to decrypt."
            )
            return

        if key == "":
            messagebox.showwarning(
                "Missing Key",
                "Please enter a decryption key."
            )
            return

        if algorithm in (
            "Caesar Cipher",
            "Additive Cipher"
        ):

            if not key.isdigit():

                messagebox.showerror(
                    "Invalid Key",
                    "Caesar and Additive ciphers require a numeric key."
                )

                return

        if algorithm == "Vigenère Cipher":

            if not key.isalpha():

                messagebox.showerror(
                    "Invalid Key",
                    "Vigenère Cipher requires alphabetic characters only."
                )

                return

        decrypted = self.encryption_engine.decrypt(
            algorithm,
            ciphertext,
            key
        )

        self.result_text.delete(
            "1.0",
            "end"
        )

        self.result_text.insert(
            "1.0",
            decrypted
        )

        self.history.save_history(
            self.staff[1],
            self.patient[0],
            self.patient[1],
            algorithm,
            key,
            "Decryption"
        )

        messagebox.showinfo(
            "Success",
            "Medical record decrypted successfully."
        )

    # ==========================================================
    # Copy Result
    # ==========================================================

    def copy_result(self):

        result = self.result_text.get(
            "1.0",
            "end"
        ).strip()

        if result == "":

            messagebox.showwarning(
                "Nothing to Copy",
                "There is no text to copy."
            )

            return

        pyperclip.copy(result)

        messagebox.showinfo(
            "Copied",
            "Encrypted text copied to clipboard."
        )

    # ==========================================================
    # Save Record
    # ==========================================================

    def save_record(self):

        encrypted = self.result_text.get(
            "1.0",
            "end"
        ).strip()

        if encrypted == "":

            messagebox.showwarning(
                "Nothing to Save",
                "Please encrypt a record first."
            )

            return

        filename = self.file_manager.save_record(
            encrypted
        )

        messagebox.showinfo(
            "Saved",
            f"Record saved successfully.\n\n{filename}"
        )

    # ==========================================================
    # Export TXT
    # ==========================================================

    def export_txt(self):

        encrypted = self.result_text.get(
            "1.0",
            "end"
        ).strip()

        if encrypted == "":

            messagebox.showwarning(
                "Nothing to Export",
                "Please encrypt a record first."
            )

            return

        self.file_manager.export_text(
            encrypted,
            self.staff[3],
            self.patient[1],
            self.patient[0],
            self.cipher_box.get(),
            self.key_entry.get()
        )

    # ==========================================================
    # Export PDF
    # ==========================================================

    def export_pdf(self):

        encrypted = self.result_text.get(
            "1.0",
            "end"
        ).strip()

        if encrypted == "":

            messagebox.showwarning(
                "Nothing to Export",
                "Please encrypt a record first."
            )

            return

        self.file_manager.export_pdf(
            encrypted,
            self.staff[3],
            self.patient[1],
            self.patient[0],
            self.cipher_box.get(),
            self.key_entry.get()
        )

    # ==========================================================
    # Open History Window
    # ==========================================================

    def open_history(self):

        HistoryWindow()

    # ==========================================================
    # Open Help Window
    # ==========================================================

    def open_help(self):

        HelpWindow()

    # ==========================================================
    # Open About Window
    # ==========================================================

    def open_about(self):

        AboutWindow()

    # ==========================================================
    # Close Dashboard
    # ==========================================================

    def on_close(self):

        try:
            self.history.close()
        except Exception:
            pass

        try:
            self.patient_manager.close()
        except Exception:
            pass

        self.destroy()

    def exit_system(self):

        answer = messagebox.askyesno(
            "Exit CipherMed",
            "Are you sure you want to exit CipherMed?"
        )

        if answer:
            self.destroy()
        else:
            self.status.configure(text="Exit cancelled.")
