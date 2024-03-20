# Developed by Rogit Sudharsan. Contact Me at rogitsudharsan81@gmail.com #

import customtkinter as ctk
import os
import sys

class ScalingApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_popup = None

        #logo
        def resource_path(relative_path):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return os.path.join(os.path.abspath("."), relative_path)

        icon_path = resource_path("logo.ico")
        self.iconbitmap(icon_path)

        self.title("Scaling Range")
        self.geometry("592x230")
        self.maxsize(592,230)
        self.minsize(592,230)
