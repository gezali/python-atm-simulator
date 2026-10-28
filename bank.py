import random
import string
import tkinter as tk
from tkinter import messagebox, ttk

CHARS = string.ascii_uppercase + string.digits


class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Bank")
        self.geometry("420x480")
        self.resizable(False, False)

        # account data
        self.name = ""
        self.age = 0
        self.address = ""
        self.pin = ""
        self.acc_no = "".join(random.choices(CHARS, k=15))
        self.balance = 0
        self.attempts = 3

        self.container = ttk.Frame(self, padding=20)
        self.container.pack(fill="both", expand=True)
        self.show_create_account()

    # ---------- helpers ----------
    def clear(self):
        for w in self.container.winfo_children():
            w.destroy()

    def heading(self, text):
        ttk.Label(self.container, text=text, font=("Segoe UI", 16, "bold")).pack(pady=(0, 15))

    def field(self, label, show=None):
        ttk.Label(self.container, text=label).pack(anchor="w")
        entry = ttk.Entry(self.container, show=show)
        entry.pack(fill="x", pady=(0, 10))
        return entry

    # ---------- screen 1: create account ----------
    def show_create_account(self):
        self.clear()
        self.heading("Create Account")
        name = self.field("Name")
        age = self.field("Age")
        address = self.field("Address")
        pin = self.field("Set a PIN (4-6 digits)", show="*")

        def submit():
            if not name.get().strip() or not address.get().strip():
                return messagebox.showerror("Error", "Name and address are required.")
            try:
                a = int(age.get())
            except ValueError:
                return messagebox.showerror("Error", "Age must be a number.")
            if a < 18:
                return messagebox.showwarning(
                    "Under age",
                    f"Sorry! You are under age.\nYou can create an account after {18 - a} year(s).",
                )
            if not (pin.get().isdigit() and 4 <= len(pin.get()) <= 6):
                return messagebox.showerror("Error", "PIN must be 4-6 digits.")

            self.name, self.age = name.get().strip(), a
            self.address, self.pin = address.get().strip(), pin.get()
            self.show_account_summary()

        ttk.Button(self.container, text="Create Account", command=submit).pack(fill="x", pady=10)

    # ---------- screen 2: account summary ----------
    def show_account_summary(self):
        self.clear()
        self.heading("Account Created")
        for label, value in [
            ("Name", self.name),
            ("Age", self.age),
            ("Address", self.address),
            ("Account no", self.acc_no),
        ]:
            row = ttk.Frame(self.container)
            row.pack(fill="x", pady=3)
            ttk.Label(row, text=f"{label}:", width=12, font=("Segoe UI", 10, "bold")).pack(side="left")
            ttk.Label(row, text=str(value), wraplength=240).pack(side="left")
        ttk.Button(self.container, text="Continue to Login", command=self.show_login).pack(fill="x", pady=25)

    # ---------- screen 3: PIN login ----------
    def show_login(self):
        self.clear()
        self.attempts = 3
        self.heading("Enter PIN")
        pin = self.field("PIN", show="*")
        status = ttk.Label(self.container, text="", foreground="red")
        status.pack()

        def verify(event=None):
            if pin.get() == self.pin:
                self.show_dashboard()
                return
            self.attempts -= 1
            pin.delete(0, "end")
            if self.attempts == 0:
                messagebox.showerror("Locked", "Too many wrong attempts. Account locked.")
                self.destroy()
            else:
                status.config(text=f"Wrong PIN. Attempts left: {self.attempts}")

        pin.bind("<Return>", verify)
        pin.focus()
        ttk.Button(self.container, text="Login", command=verify).pack(fill="x", pady=10)

    # ---------- screen 4: dashboard ----------
    def show_dashboard(self):
        self.clear()
        self.heading(f"Welcome, {self.name}")
        ttk.Label(self.container, text=f"Account: {self.acc_no}").pack()

        self.balance_var = tk.StringVar()
        self.update_balance()
        ttk.Label(self.container, text="Current Balance", font=("Segoe UI", 10)).pack(pady=(20, 0))
        ttk.Label(self.container, textvariable=self.balance_var, font=("Segoe UI", 26, "bold")).pack(pady=(0, 20))

        amount = self.field("Amount")

        def get_amount():
            try:
                value = int(amount.get())
                if value <= 0:
                    raise ValueError
                return value
            except ValueError:
                messagebox.showerror("Error", "Enter a valid positive amount.")
                return None

        def deposit():
            value = get_amount()
            if value is None:
                return
            self.balance += value
            self.update_balance()
            amount.delete(0, "end")
            messagebox.showinfo("Deposit", f"You deposited {value}.\nNew balance: {self.balance}")

        def withdraw():
            value = get_amount()
            if value is None:
                return
            if value > self.balance:
                return messagebox.showwarning("Low balance", "Insufficient balance.")
            self.balance -= value
            self.update_balance()
            amount.delete(0, "end")
            messagebox.showinfo("Withdraw", f"You withdrew {value}.\nNew balance: {self.balance}")

        btns = ttk.Frame(self.container)
        btns.pack(fill="x", pady=5)
        ttk.Button(btns, text="Deposit", command=deposit).pack(side="left", expand=True, fill="x", padx=(0, 5))
        ttk.Button(btns, text="Withdraw", command=withdraw).pack(side="left", expand=True, fill="x", padx=(5, 0))

        def exit_app():
            messagebox.showinfo("Goodbye", "Thank you for choosing our service")
            self.destroy()

        ttk.Button(self.container, text="Exit", command=exit_app).pack(fill="x", pady=20)

    def update_balance(self):
        self.balance_var.set(f"₹ {self.balance:,}")


if __name__ == "__main__":
    BankApp().mainloop()
