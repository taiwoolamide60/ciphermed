
"""
===============================================================================
CipherMed Secure Medical Information Encryption System

Module:
    Login Window

Purpose:
    Authenticates hospital staff before allowing access to the system.

Author:
    TAIWO OLAMIDE AKINBOBOLA
===============================================================================
"""

# =============================================================================
# Import Libraries
# =============================================================================

import customtkinter as ctk
from tkinter import messagebox

from modules.authentication import Authentication
from modules.validation import Validation
from modules import theme

from ui.dashboard import Dashboard


# =============================================================================
# Login Window
# =============================================================================

class LoginWindow(ctk.CTk):
    """
    CipherMed Login Window.
    """

    def __init__(self):

        super().__init__()

        # ------------------------------------------------------------------
        # Window Settings
        # ------------------------------------------------------------------

        self.title("CipherMed Login")
        self.geometry("1100x700")

        try:
            self.iconbitmap("assets/icon.ico")
        except Exception:
            pass

        self.resizable(False, False)
        self.configure(fg_color=theme.BACKGROUND)

        # ------------------------------------------------------------------
        # Authentication Module
        # ------------------------------------------------------------------

        self.authentication = Authentication()

        # ------------------------------------------------------------------
        # Validation Module
        # ------------------------------------------------------------------

        self.validation = Validation()

        # ------------------------------------------------------------------
        # Main Container
        # ------------------------------------------------------------------

        self.main_frame = ctk.CTkFrame(
            self,
            fg_color="white",
            corner_radius=20
        )

        self.main_frame.pack(
            padx=25,
            pady=25,
            fill="both",
            expand=True
        )

        # ------------------------------------------------------------------
        # Left Branding Panel
        # ------------------------------------------------------------------

        self.left_panel = ctk.CTkFrame(
            self.main_frame,
            width=360,
            fg_color=theme.HEADER,
            corner_radius=15
        )

        self.left_panel.pack(
            side="left",
            fill="y",
            padx=20,
            pady=20
        )

        self.left_panel.pack_propagate(False)

        # ------------------------------------------------------------------
        # Right Login Panel
        # ------------------------------------------------------------------

        self.right_panel = ctk.CTkFrame(
            self.main_frame,
            fg_color="white",
            corner_radius=15
        )

        self.right_panel.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(0, 20),
            pady=20
        )

        # ------------------------------------------------------------------
        # Logo
        # ------------------------------------------------------------------

        self.logo = ctk.CTkLabel(
            self.left_panel,
            text="🛡",
            font=("Segoe UI Emoji", 70),
            text_color="white"
        )

        self.logo.pack(pady=(60, 20))

        self.system_title = ctk.CTkLabel(
            self.left_panel,
            text="CipherMed",
            font=theme.TITLE_FONT,
            text_color="white"
        )

        self.system_title.pack()

        self.description = ctk.CTkLabel(
            self.left_panel,
            text=(
                "Secure Medical Information\n"
                "Encryption System\n\n"
                "Protecting confidential patient\n"
                "records using classical\n"
                "cryptographic algorithms."
            ),
            justify="center",
            font=theme.BODY_FONT,
            text_color="white"
        )

        self.description.pack(pady=20)

        self.version = ctk.CTkLabel(
            self.left_panel,
            text="Version 1.0",
            font=theme.BODY_FONT,
            text_color="#DDE9F5"
        )

        self.version.pack(side="bottom", pady=35)

        # ------------------------------------------------------------------
        # Login Header
        # ------------------------------------------------------------------

        self.login_title = ctk.CTkLabel(
            self.right_panel,
            text="Welcome Back",
            font=theme.TITLE_FONT,
            text_color=theme.TEXT
        )

        self.login_title.pack(
            pady=(60, 10)
        )

        self.login_subtitle = ctk.CTkLabel(
            self.right_panel,
            text="Authenticate to access CipherMed Secure Records",
            font=theme.BODY_FONT,
            text_color=theme.SUBTEXT
        )

        self.login_subtitle.pack()

        # ------------------------------------------------------------------
        # Username Input
        # ------------------------------------------------------------------

        self.username_label = ctk.CTkLabel(
            self.right_panel,
            text="Staff Username",
            font=theme.BODY_FONT
        )

        self.username_label.pack(
            anchor="w",
            padx=80,
            pady=(40, 5)
        )

        self.username_entry = ctk.CTkEntry(
            self.right_panel,
            width=350,
            height=40,
            placeholder_text="Enter username"
        )

        self.username_entry.pack()

        # ------------------------------------------------------------------
        # Password Input
        # ------------------------------------------------------------------

        self.password_label = ctk.CTkLabel(
            self.right_panel,
            text="Password",
            font=theme.BODY_FONT
        )

        self.password_label.pack(
            anchor="w",
            padx=80,
            pady=(20, 5)
        )

        self.password_entry = ctk.CTkEntry(
            self.right_panel,
            width=350,
            height=40,
            placeholder_text="Enter password",
            show="●"
        )

        self.password_entry.pack()

        # ------------------------------------------------------------------
        # Department Selection
        # ------------------------------------------------------------------

        self.department_label = ctk.CTkLabel(
            self.right_panel,
            text="Department",
            font=theme.BODY_FONT
        )

        self.department_label.pack(
            anchor="w",
            padx=80,
            pady=(20, 5)
        )

        self.department_box = ctk.CTkComboBox(
            self.right_panel,
            width=350,
            values=[
                "Administration",
                "Respiratory",
                "Nursing",
                "Pharmacy"
            ]
        )

        self.department_box.pack()

        self.department_box.set("Select Department")

        # ------------------------------------------------------------------
        # Remember Username
        # ------------------------------------------------------------------

        self.remember = ctk.CTkCheckBox(
            self.right_panel,
            text="Remember Username",
            font=theme.BODY_FONT
        )

        self.remember.pack(
            pady=20
        )

        # ------------------------------------------------------------------
        # Button Container
        # ------------------------------------------------------------------

        self.button_frame = ctk.CTkFrame(
            self.right_panel,
            fg_color="transparent"
        )

        self.button_frame.pack(
            pady=20
        )

        self.login_button = ctk.CTkButton(
            self.button_frame,
            text="LOGIN",
            width=120,
            height=40,
            font=theme.BUTTON_FONT,
            command=self.login
        )

        self.login_button.grid(
            row=0,
            column=0,
            padx=10
        )

        self.clear_button = ctk.CTkButton(
            self.button_frame,
            text="CLEAR",
            width=120,
            height=40,
            fg_color=theme.SECONDARY,
            text_color=theme.TEXT,
            command=self.clear_fields
        )

        self.clear_button.grid(
            row=0,
            column=1,
            padx=10
        )

        self.exit_button = ctk.CTkButton(
            self.button_frame,
            text="EXIT",
            width=120,
            height=40,
            fg_color=theme.ERROR,
            command=self.destroy
        )

        self.exit_button.grid(
            row=0,
            column=2,
            padx=10
        )

        # ------------------------------------------------------------------
        # Status Message
        # ------------------------------------------------------------------

        self.status = ctk.CTkLabel(
            self.right_panel,
            text="Status: Waiting for authentication...",
            font=theme.STATUS_FONT,
            text_color=theme.SUBTEXT,
            height=35,
            wraplength=450
        )

        self.status.pack(
            pady=(10, 20),
            padx=20
        )

    # =========================================================================
    # Login Authentication
    # =========================================================================

    def login(self):

        username = self.username_entry.get()
        password = self.password_entry.get()
        department = self.department_box.get()

        # Validate user input
        valid, message = self.validation.validate_login_input(
            username,
            password,
            department
        )

        if not valid:
            messagebox.showwarning(
                "Incomplete Information",
                message
            )
            return

        # Authenticate user
        user = self.authentication.login(
            username,
            password,
            department
        )

        print(user)

        if user:

            self.status.configure(
                text="Status: Authentication successful"
            )

            messagebox.showinfo(
                "Login Successful",
                f"Welcome {username}"
            )

            self.destroy()

            dashboard = Dashboard(user)
            dashboard.mainloop()

        else:

            self.status.configure(
                text="Status: Invalid credentials"
            )

            messagebox.showerror(
                "Access Denied",
                "Invalid username, password or department."
            )

    def clear_fields(self):

        self.username_entry.delete(0, "end")

        self.password_entry.delete(0, "end")

        self.department_box.set("Select Department")

        self.status.configure(
            text="Status: Waiting for authentication..."
        )
