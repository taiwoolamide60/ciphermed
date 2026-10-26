"""
===========================================================================
CipherMed Secure Medical Information Encryption System
Splash Screen Module

Purpose:
    Displays the application splash screen while CipherMed loads.

Author:
    Your Name

=========================================================================== 
"""

# -------------------------------------------------------------------------
# Import Required Libraries
# -------------------------------------------------------------------------

import customtkinter as ctk
from PIL import Image
import os
from ui.login import LoginWindow


# -------------------------------------------------------------------------
# Splash Screen Class
# -------------------------------------------------------------------------

class SplashScreen(ctk.CTk):

    """
    Splash screen displayed when CipherMed starts.
    """

    def __init__(self):

        super().__init__()

        # -------------------------------------------------------------
        # Window Configuration
        # -------------------------------------------------------------

        self.title("CipherMed")

        self.geometry("900x550")
        try:
            self.iconbitmap("assets/icon.ico")
        except Exception:
            pass

        self.resizable(False, False)

        ctk.set_appearance_mode("light")

        ctk.set_default_color_theme("blue")

        # -------------------------------------------------------------
        # Background Colour
        # -------------------------------------------------------------

        self.configure(fg_color="#F5F9FC")

        # -------------------------------------------------------------
        # Main Container
        # -------------------------------------------------------------

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

        # -------------------------------------------------------------
        # Hospital Icon
        # -------------------------------------------------------------

        self.logo_label = ctk.CTkLabel(
            self.main_frame,
            text="🏥",
            font=("Segoe UI Emoji", 70)
        )

        self.logo_label.pack(pady=(35, 10))

        # -------------------------------------------------------------
        # System Title
        # -------------------------------------------------------------

        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="CipherMed",
            font=("Segoe UI", 34, "bold"),
            text_color="#0F4C81"
        )

        self.title_label.pack()

        # -------------------------------------------------------------
        # Subtitle
        # -------------------------------------------------------------

        self.subtitle = ctk.CTkLabel(
            self.main_frame,
            text="Secure Medical Information Encryption System",
            font=("Segoe UI", 17),
            text_color="#4B5563"
        )

        self.subtitle.pack(pady=(5, 20))

        # -------------------------------------------------------------
        # Hospital Name
        # -------------------------------------------------------------

        self.company = ctk.CTkLabel(
            self.main_frame,
            text="CipherCare Medical Centre",
            font=("Segoe UI", 18, "bold"),
            text_color="#16A34A"
        )

        self.company.pack()

        # -------------------------------------------------------------
        # Version Number
        # -------------------------------------------------------------

        self.version = ctk.CTkLabel(
            self.main_frame,
            text="Version 1.0",
            font=("Segoe UI", 13)
        )

        self.version.pack(pady=(5, 35))

        # -------------------------------------------------------------
        # Progress Bar
        # -------------------------------------------------------------

        self.progress = ctk.CTkProgressBar(
            self.main_frame,
            width=500,
            progress_color="#2563EB"
        )

        self.progress.pack()

        self.progress.set(0)

        # -------------------------------------------------------------
        # Loading Message
        # -------------------------------------------------------------

        self.status = ctk.CTkLabel(
            self.main_frame,
            text="Loading application...",
            font=("Segoe UI", 13)
        )

        self.status.pack(pady=15)

        # -------------------------------------------------------------
        # Copyright
        # -------------------------------------------------------------

        self.footer = ctk.CTkLabel(
            self.main_frame,
            text="© 2026 CipherCare Medical Centre",
            font=("Segoe UI", 11),
            text_color="gray50"
        )

        self.footer.pack(side="bottom", pady=15)

        # -------------------------------------------------------------
        # Begin Loading Animation
        # -------------------------------------------------------------

        self.loading_value = 0

        self.animate_progress()

    # -----------------------------------------------------------------
    # Progress Bar Animation
    # -----------------------------------------------------------------

    def animate_progress(self):

        """
        Animates the loading progress bar.
        """

        if self.loading_value <= 100:

            self.progress.set(self.loading_value / 100)

            self.loading_value += 2

            self.after(40, self.animate_progress)

        else:

            self.withdraw()

            login = LoginWindow()

            login.mainloop()

            self.destroy()          

            