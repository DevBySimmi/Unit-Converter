import tkinter as tk


class UnitConverter:

    def __init__(self, root):
        self.root = root

        self.root.title("📏 Unit Converter")
        self.root.geometry("600x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#10151c")

        self.create_ui()

    # =====================================================
    # CREATE UI
    # =====================================================

    def create_ui(self):

        # Title
        tk.Label(
            self.root,
            text="📏 UNIT CONVERTER",
            font=("Consolas", 26, "bold"),
            fg="#63e6be",
            bg="#10151c"
        ).pack(pady=(30, 5))

        tk.Label(
            self.root,
            text="Convert units quickly and easily",
            font=("Consolas", 10),
            fg="#7d8794",
            bg="#10151c"
        ).pack()

        # Category
        tk.Label(
            self.root,
            text="Category",
            font=("Consolas", 11, "bold"),
            fg="white",
            bg="#10151c"
        ).pack(pady=(30, 5))

        self.category_var = tk.StringVar(
            value="Length"
        )

        category_menu = tk.OptionMenu(
            self.root,
            self.category_var,
            "Length",
            "Weight",
            "Temperature",
            "Volume",
            command=self.update_units
        )

        category_menu.config(
            font=("Consolas", 11, "bold"),
            bg="#252e39",
            fg="white",
            activebackground="#344150",
            activeforeground="white",
            relief="flat",
            width=18
        )

        category_menu["menu"].config(
            bg="#252e39",
            fg="white",
            font=("Consolas", 10)
        )

        category_menu.pack()

        # Input
        tk.Label(
            self.root,
            text="Enter Value",
            font=("Consolas", 11, "bold"),
            fg="white",
            bg="#10151c"
        ).pack(pady=(25, 5))

        self.value_entry = tk.Entry(
            self.root,
            font=("Consolas", 16, "bold"),
            justify="center",
            bg="#252e39",
            fg="white",
            insertbackground="white",
            relief="flat",
            width=20
        )

        self.value_entry.pack(
            ipady=10
        )

        # From / To frame
        units_frame = tk.Frame(
            self.root,
            bg="#10151c"
        )
        units_frame.pack(pady=25)

        # From
        tk.Label(
            units_frame,
            text="From",
            font=("Consolas", 11, "bold"),
            fg="white",
            bg="#10151c"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=5
        )

        self.from_var = tk.StringVar()

        self.from_menu = tk.OptionMenu(
            units_frame,
            self.from_var,
            ""
        )

        self.from_menu.config(
            font=("Consolas", 10, "bold"),
            bg="#252e39",
            fg="white",
            activebackground="#344150",
            activeforeground="white",
            relief="flat",
            width=12
        )

        self.from_menu["menu"].config(
            bg="#252e39",
            fg="white",
            font=("Consolas", 10)
        )

        self.from_menu.grid(
            row=1,
            column=0,
            padx=10
        )

        # Arrow
        tk.Label(
            units_frame,
            text="→",
            font=("Consolas", 20, "bold"),
            fg="#63e6be",
            bg="#10151c"
        ).grid(
            row=1,
            column=1,
            padx=5
        )

        # To
        tk.Label(
            units_frame,
            text="To",
            font=("Consolas", 11, "bold"),
            fg="white",
            bg="#10151c"
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=5
        )

        self.to_var = tk.StringVar()

        self.to_menu = tk.OptionMenu(
            units_frame,
            self.to_var,
            ""
        )

        self.to_menu.config(
            font=("Consolas", 10, "bold"),
            bg="#252e39",
            fg="white",
            activebackground="#344150",
            activeforeground="white",
            relief="flat",
            width=12
        )

        self.to_menu["menu"].config(
            bg="#252e39",
            fg="white",
            font=("Consolas", 10)
        )

        self.to_menu.grid(
            row=1,
            column=2,
            padx=10
        )

        # Convert button
        tk.Button(
            self.root,
            text="⇄ CONVERT",
            command=self.convert,
            font=("Consolas", 11, "bold"),
            bg="#63e6be",
            fg="#10151c",
            activebackground="#80f0ce",
            relief="flat",
            cursor="hand2",
            padx=30,
            pady=12
        ).pack(pady=10)

        # Result box
        result_frame = tk.Frame(
            self.root,
            bg="#191f28",
            width=500,
            height=100
        )

        result_frame.pack(
            padx=50,
            pady=20
        )

        result_frame.pack_propagate(False)

        self.result_label = tk.Label(
            result_frame,
            text="Result will appear here",
            font=("Consolas", 15, "bold"),
            fg="white",
            bg="#191f28"
        )

        self.result_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # Clear button
        tk.Button(
            self.root,
            text="↻ CLEAR",
            command=self.clear,
            font=("Consolas", 10, "bold"),
            bg="#252e39",
            fg="white",
            activebackground="#344150",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=8
        ).pack()

        # Load initial units
        self.update_units("Length")

    # =====================================================
    # UPDATE UNITS
    # =====================================================

    def update_units(self, category):

        units = {

            "Length": [
                "Millimeter",
                "Centimeter",
                "Meter",
                "Kilometer"
            ],

            "Weight": [
                "Milligram",
                "Gram",
                "Kilogram"
            ],

            "Temperature": [
                "Celsius",
                "Fahrenheit",
                "Kelvin"
            ],

            "Volume": [
                "Milliliter",
                "Liter"
            ]
        }

        unit_list = units[category]

        self.from_var.set(unit_list[0])
        self.to_var.set(unit_list[1])

        self.from_menu["menu"].delete(
            0,
            "end"
        )

        self.to_menu["menu"].delete(
            0,
            "end"
        )

        for unit in unit_list:

            self.from_menu["menu"].add_command(
                label=unit,
                command=lambda value=unit:
                self.from_var.set(value)
            )

            self.to_menu["menu"].add_command(
                label=unit,
                command=lambda value=unit:
                self.to_var.set(value)
            )

        self.result_label.config(
            text="Result will appear here"
        )

    # =====================================================
    # CONVERT
    # =====================================================

    def convert(self):

        try:
            value = float(
                self.value_entry.get()
            )

        except ValueError:

            self.result_label.config(
                text="⚠️ Please enter a valid number.",
                fg="#ffd166"
            )

            return

        category = self.category_var.get()
        from_unit = self.from_var.get()
        to_unit = self.to_var.get()

        try:

            if category == "Length":

                result = self.convert_length(
                    value,
                    from_unit,
                    to_unit
                )

            elif category == "Weight":

                result = self.convert_weight(
                    value,
                    from_unit,
                    to_unit
                )

            elif category == "Temperature":

                result = self.convert_temperature(
                    value,
                    from_unit,
                    to_unit
                )

            else:

                result = self.convert_volume(
                    value,
                    from_unit,
                    to_unit
                )

            self.result_label.config(
                text=f"{value:g} {from_unit} = "
                     f"{result:.4f} {to_unit}",
                fg="#63e6be"
            )

        except Exception:

            self.result_label.config(
                text="⚠️ Conversion error.",
                fg="#ff6b6b"
            )

    # =====================================================
    # LENGTH
    # =====================================================

    def convert_length(
        self,
        value,
        from_unit,
        to_unit
    ):

        factors = {
            "Millimeter": 0.001,
            "Centimeter": 0.01,
            "Meter": 1,
            "Kilometer": 1000
        }

        meters = value * factors[from_unit]

        return meters / factors[to_unit]

    # =====================================================
    # WEIGHT
    # =====================================================

    def convert_weight(
        self,
        value,
        from_unit,
        to_unit
    ):

        factors = {
            "Milligram": 0.001,
            "Gram": 1,
            "Kilogram": 1000
        }

        grams = value * factors[from_unit]

        return grams / factors[to_unit]

    # =====================================================
    # TEMPERATURE
    # =====================================================

    def convert_temperature(
        self,
        value,
        from_unit,
        to_unit
    ):

        # Convert to Celsius first

        if from_unit == "Celsius":
            celsius = value

        elif from_unit == "Fahrenheit":
            celsius = (value - 32) * 5 / 9

        else:
            celsius = value - 273.15

        # Celsius to target

        if to_unit == "Celsius":
            return celsius

        elif to_unit == "Fahrenheit":
            return (celsius * 9 / 5) + 32

        else:
            return celsius + 273.15

    # =====================================================
    # VOLUME
    # =====================================================

    def convert_volume(
        self,
        value,
        from_unit,
        to_unit
    ):

        factors = {
            "Milliliter": 0.001,
            "Liter": 1
        }

        liters = value * factors[from_unit]

        return liters / factors[to_unit]

    # =====================================================
    # CLEAR
    # =====================================================

    def clear(self):

        self.value_entry.delete(
            0,
            tk.END
        )

        self.result_label.config(
            text="Result will appear here",
            fg="white"
        )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = UnitConverter(root)

    root.mainloop()