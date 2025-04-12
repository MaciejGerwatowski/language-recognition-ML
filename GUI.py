import tkinter as tk
from tkinter.constants import TOP, BOTTOM

import Methods as m
import Methods2 as m2


class GUI:
    def __init__(self):
        self.clicked = False
        self.root = tk.Tk()
        self.root.title("Language detector")

        # Pole tekstowe
        self.text = tk.Text(self.root, height=8)
        self.text.pack(padx=10, pady=10, expand=True, fill=tk.BOTH, side=TOP)

        self.activation_type = tk.StringVar(self.root)
        self.activation_type.set("Unipolar")
        self.dropdown = tk.OptionMenu(self.root, self.activation_type, "Unipolar", "Bipolar")
        self.dropdown.pack(padx=10, pady=5, side=BOTTOM)

        # Przycisk
        self.myButton = tk.Button(self.root, text="Detect language", command=self.check)
        self.myButton.pack(padx=10, pady=10, expand=True, side=BOTTOM)

        self.label = tk.Label(self.root, text="")
        self.label.pack(padx=5, pady=5, side=BOTTOM)

        self.root.mainloop()

    def check(self):
        user_text = self.text.get("1.0", tk.END).strip()
        activation = self.activation_type.get()

        if activation == "Unipolar":
            result = m.classify(user_text)
        elif activation == "Bipolar":
            result = m2.classify2(user_text)
        else:
            result = "Unknown activation function"

        self.label["text"] = result