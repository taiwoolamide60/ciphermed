"""
===============================================================================
CipherMed Secure Medical Information Encryption System

Module Name : file_manager.py

Purpose:
    Handles saving and exporting encrypted medical records.

Responsibilities:
    • Save encrypted records.
    • Export encrypted records to TXT.
    • Export encrypted records to PDF.

Author:
    TAIWO OLAMIDE AKINBOBOLA
===============================================================================
"""

import os
from datetime import datetime

from tkinter import filedialog

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
class FileManager:

    """
    Handles all CipherMed file operations.
    """

    def __init__(self):

        self.records_folder = "records"

        os.makedirs(

            self.records_folder,

            exist_ok=True

        )
    def save_record(self, encrypted_text):

        timestamp = datetime.now().strftime(

        "%Y%m%d_%H%M%S"

    )

        filename = os.path.join(

        self.records_folder,

        f"CipherMed_Record_{timestamp}.txt"

    )

        with open(

        filename,

        "w",

        encoding="utf-8"

    )   as file:

         file.write(encrypted_text)

        return filename
    def export_text(

        self,

        encrypted_text,

        staff_name,

        patient_name,

        patient_id,

        cipher,

        key

):

        filename = filedialog.asksaveasfilename(

        defaultextension=".txt",

        filetypes=[

            ("Text File","*.txt")

        ]

    )

        if not filename:

         return

        with open(

        filename,

        "w",

        encoding="utf-8"

    )   as file:

         file.write(

         f"""CipherMed Secure Medical Information Encryption System

        Staff
        {staff_name}

        Patient
        {patient_name}

        Patient ID
        {patient_id}

        Cipher
        {cipher}

        Encryption Key
        {key}

        Generated
        {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}

        Encrypted Medical Record

        {encrypted_text}
"""
        )
    def export_pdf(

        self,

        encrypted_text,

        staff_name,

        patient_name,

        patient_id,

        cipher,

        key

):

        filename = filedialog.asksaveasfilename(

        defaultextension=".pdf",

        filetypes=[

            ("PDF File","*.pdf")

        ]

    )

        if not filename:

         return
        document = SimpleDocTemplate(

        filename

    )

        styles = getSampleStyleSheet()

        story = []
        story.append(

        Paragraph(

            "<b>CipherMed Secure Medical Information Encryption System</b>",

            styles["Title"]

        )

    )
        story.append(

        Paragraph(

            f"<b>Staff:</b> {staff_name}",

            styles["BodyText"]

        )

    )
        story.append(

        Paragraph(

            f"<b>Patient:</b> {patient_name}",

            styles["BodyText"]

        )

    )

        story.append(

        Paragraph(

            f"<b>Patient ID:</b> {patient_id}",

            styles["BodyText"]

        )

    )
        story.append(

        Paragraph(

            f"<b>Cipher:</b> {cipher}",

            styles["BodyText"]

        )

    )

        story.append(

        Paragraph(

            f"<b>Encryption Key:</b> {key}",

            styles["BodyText"]

        )

    )
        story.append(

        Paragraph(

            f"<b>Generated:</b> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",

            styles["BodyText"]

        )

    )
        story.append(

        Paragraph(

            "<br/><b>Encrypted Medical Record</b>",

            styles["Heading2"]

        )

    )

        story.append(

        Paragraph(

            encrypted_text.replace(

                "\n",

                "<br/>"

            ),

            styles["BodyText"]

        )

    )
        document.build(

        story

    )