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

        # Header frame
        self.header_frame = ctk.CTkFrame(self, width=322, height=50)
        self.header_frame.pack_propagate(True)
        self.header_frame.place(x=10, y=167)

        header_label = ctk.CTkLabel(self.header_frame, text="Scaling Range", font=ctk.CTkFont(size=15, weight="bold"))
        header_label.place(relx=0.5, rely=0.5, anchor="center")

        # Frame1 for first set of inputs (x1, x2, y1, y2, z1, z2)
        self.frame1 = ctk.CTkFrame(self, width=490, height=290)
        self.frame1.place(x=10, y=10)
        self.frame1.pack_propagate(True)

        self.entry_x1 = ctk.CTkEntry(self.frame1, placeholder_text="X1")
        self.entry_x1.grid(row=0, column=1, padx=10, pady=10)

        self.entry_x2 = ctk.CTkEntry(self.frame1, placeholder_text="X2")
        self.entry_x2.grid(row=0, column=3, padx=10, pady=10)

        self.entry_y1 = ctk.CTkEntry(self.frame1, placeholder_text="Y1")
        self.entry_y1.grid(row=1, column=1, padx=10, pady=10)

        self.entry_y2 = ctk.CTkEntry(self.frame1, placeholder_text="Y2")
        self.entry_y2.grid(row=1, column=3, padx=10, pady=10)

        self.entry_z1 = ctk.CTkEntry(self.frame1, placeholder_text="Z1")
        self.entry_z1.grid(row=2, column=1, padx=10, pady=10)

        self.entry_z2 = ctk.CTkEntry(self.frame1, placeholder_text="Z2")
        self.entry_z2.grid(row=2, column=3, padx=10, pady=10)

        # Frame2 for second set of inputs (X, Y, Z)
        self.frame2 = ctk.CTkFrame(self, width=350, height=290)
        self.frame2.place(x=342, y=10)
        self.frame2.pack_propagate(True)

        self.var = ctk.IntVar(value=0)
        self.radio_x = ctk.CTkRadioButton(self.frame2, radiobutton_height=20, radiobutton_width=20, border_width_unchecked=2, text="", variable=self.var, value=0, command=self.update_entry_states)
        self.radio_x.grid(row=0, column=0, padx=(25,0), pady=10, sticky="w")
        self.radio_y = ctk.CTkRadioButton(self.frame2, radiobutton_height=20, radiobutton_width=20, border_width_unchecked=2, text="", variable=self.var, value=1, command=self.update_entry_states)
        self.radio_y.grid(row=1, column=0, padx=(25,0), pady=10, sticky="w")
        self.radio_z = ctk.CTkRadioButton(self.frame2, radiobutton_height=20, radiobutton_width=20, border_width_unchecked=2, text="", variable=self.var, value=2, command=self.update_entry_states)
        self.radio_z.grid(row=2, column=0, padx=(25,0), pady=10, sticky="w")

        self.entry_x = ctk.CTkEntry(self.frame2, placeholder_text="X")
        self.entry_x.grid(row=0, column=0, padx=(70,30), pady=10)

        self.entry_y = ctk.CTkEntry(self.frame2, placeholder_text="Y")
        self.entry_y.grid(row=1, column=0, padx=(70,30), pady=10)

        self.entry_z = ctk.CTkEntry(self.frame2, placeholder_text="Z")
        self.entry_z.grid(row=2, column=0, padx=(70,30), pady=10)

        # Frame3 for the Z in HEX functionality
        self.frame3 = ctk.CTkFrame(self, width=240, height=50)
        self.frame3.place(x=342, y=167)

        self.z_in_hex_var = ctk.BooleanVar(value=False)
        self.checkbox_z_in_hex = ctk.CTkCheckBox(self.frame3, checkbox_height=20, checkbox_width=20, border_width=2, text="Z in HEX", variable=self.z_in_hex_var, command=self.calculate)
        self.checkbox_z_in_hex.place(relx=0.5, rely=0.5, anchor="center")

        # Trace input changes for immediate calculation upon change.
        self.entry_x1.bind("<KeyRelease>", self.calculate)
        self.entry_x2.bind("<KeyRelease>", self.calculate)
        self.entry_y1.bind("<KeyRelease>", self.calculate)
        self.entry_y2.bind("<KeyRelease>", self.calculate)
        self.entry_z1.bind("<KeyRelease>", self.calculate)
        self.entry_z2.bind("<KeyRelease>", self.calculate)
        self.entry_x.bind("<KeyRelease>", self.calculate)
        self.entry_y.bind("<KeyRelease>", self.calculate)
        self.entry_z.bind("<KeyRelease>", self.calculate)

        self.update_entry_states()

    # Selected radio = write privilege ; Else = readonly.
    def update_entry_states(self):
        selected_value = self.var.get()
        if selected_value == 0:
            self.entry_x.configure(state="normal")
            self.entry_y.configure(state="readonly")
            self.entry_z.configure(state="readonly")
        elif selected_value == 1:
            self.entry_x.configure(state="readonly")
            self.entry_y.configure(state="normal")
            self.entry_z.configure(state="readonly")
        elif selected_value == 2:
            self.entry_x.configure(state="readonly")
            self.entry_y.configure(state="readonly")
            self.entry_z.configure(state="normal")

    def calculate(self, event=None):
        try:
            x1 = self.validate_entry(self.entry_x1)
            x2 = self.validate_entry(self.entry_x2)
            y1 = self.validate_entry(self.entry_y1)
            y2 = self.validate_entry(self.entry_y2)
            z1 = self.validate_entry(self.entry_z1)
            z2 = self.validate_entry(self.entry_z2)

            # Check for None values before performing calculations
            if any(val is None for val in [x1, x2, y1, y2, z1, z2]):
                return

            selected_value = self.var.get()

            if selected_value == 0:  # Calculate Y and Z based on X
                input_val = self.validate_entry(self.entry_x)
                if input_val is None:
                    return
                y = self._calculate_scaled_value(input_val, x1, x2, y1, y2)
                z = self._calculate_scaled_value(input_val, x1, x2, z1, z2)
                self.display_result(self.entry_y, y)
                self.display_result(self.entry_z, z)

            elif selected_value == 1:  # Calculate X and Z based on Y
                input_val = self.validate_entry(self.entry_y)
                if input_val is None:
                    return
                x = self._calculate_scaled_value(input_val, y1, y2, x1, x2)
                z = self._calculate_scaled_value(input_val, y1, y2, z1, z2)
                self.display_result(self.entry_x, x)
                self.display_result(self.entry_z, z)

            elif selected_value == 2:  # Calculate X and Y based on Z
                input_val = self.validate_entry(self.entry_z)
                if input_val is None:
                    return
                x = self._calculate_scaled_value(input_val, z1, z2, x1, x2)
                y = self._calculate_scaled_value(input_val, z1, z2, y1, y2)
                self.display_result(self.entry_x, x)
                self.display_result(self.entry_y, y)

        except (ZeroDivisionError, ValueError) as e:
            self.display_error(str(e), event.widget if event else self)

    @staticmethod
    def _calculate_scaled_value(input_value, input_start, input_end, output_start, output_end):
        if (input_end - input_start) == 0:
            raise ZeroDivisionError("Input range cannot be zero.")
        slope = (output_end - output_start) / (input_end - input_start)
        intercept = output_start - (slope * input_start)
        return slope * input_value + intercept
