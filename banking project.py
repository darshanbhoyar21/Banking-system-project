import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import random

class BankingSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Banking System")
        self.root.configure(bg='yellow')  # Set the background color of the root window

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), padding=5, background='white', foreground='black')
        self.style.configure('TLabel', font=('Helvetica', 14), background='black', foreground='white')
        self.style.configure('TEntry', font=('Helvetica', 12), padding=5, background='#D3D3D3')

        self.account_number = None
        self.pin = None
        self.balance = 0

        self.login_page()

    def login_page(self):
        self.clear_screen()

        label = ttk.Label(self.root, text="Login", style='TLabel')
        label.pack(pady=10)

        create_account_button = ttk.Button(self.root, text="Create Account", command=self.create_account_page)
        create_account_button.pack(pady=5)

        login_button = ttk.Button(self.root, text="Login", command=self.validate_login)
        login_button.pack(pady=5)

    def create_account_page(self):
        self.clear_screen()

        label = ttk.Label(self.root, text="Create Account", style='TLabel')
        label.pack(pady=10)

        self.account_number = self.generate_account_number()
        label_account = ttk.Label(self.root, text=f"Account Number: {self.account_number}", style='TLabel')
        label_account.pack()

        label_pin = ttk.Label(self.root, text="Enter 4-digit PIN:", style='TLabel')
        label_pin.pack(pady=5)

        pin_entry = ttk.Entry(self.root, show="*")
        pin_entry.pack(pady=5)

        create_button = ttk.Button(self.root, text="Create Account", command=lambda: self.create_account(pin_entry.get()))
        create_button.pack(pady=10)

    def generate_account_number(self):
        return random.randint(10000000, 99999999)

    def create_account(self, pin):
        print(f"Account Created!\nAccount Number: {self.account_number}\nPIN: {pin}")
        self.login_page()

    def validate_login(self):
        self.clear_screen()

        label = ttk.Label(self.root, text="Login", style='TLabel')
        label.pack(pady=10)

        label_account = ttk.Label(self.root, text="Enter Account Number:", style='TLabel')
        label_account.pack(pady=5)

        account_entry = ttk.Entry(self.root)
        account_entry.pack(pady=5)

        label_pin = ttk.Label(self.root, text="Enter 4-digit PIN:", style='TLabel')
        label_pin.pack(pady=5)

        pin_entry = ttk.Entry(self.root, show="*")
        pin_entry.pack(pady=5)

        login_button = ttk.Button(self.root, text="Login", command=lambda: self.login(account_entry.get(), pin_entry.get()))
        login_button.pack(pady=10)

    def login(self, account_number, pin):
        if account_number == str(self.account_number) and pin == "1234":  # Change "1234" with the actual pin
            self.main_menu_page()
        else:
            messagebox.showerror("Error", "Invalid account number or PIN. Try again.")

    def main_menu_page(self):
        self.clear_screen()

        label = ttk.Label(self.root, text="Main Menu", style='TLabel')
        label.pack(pady=10)

        balance_label = ttk.Label(self.root, text=f"Balance:₹{self.balance}", style='TLabel')
        balance_label.pack()

        deposit_button = ttk.Button(self.root, text="Deposit", command=self.deposit_page)
        deposit_button.pack(pady=10)

        withdraw_button = ttk.Button(self.root, text="Withdraw", command=self.withdraw_page)
        withdraw_button.pack(pady=10)

        logout_button = ttk.Button(self.root, text="Logout", command=self.logout)
        logout_button.pack(pady=10)

    def deposit_page(self):
        amount = simpledialog.askinteger("Deposit", "Enter the amount to deposit:")
        if amount is not None and amount > 0:
            self.balance += amount
            messagebox.showinfo("Deposit", f"Amount deposited: ${amount}\nNew Balance: ${self.balance}")
            self.main_menu_page()
        else:
            messagebox.showwarning("Deposit", "Invalid amount. Please enter a positive value.")

    def withdraw_page(self):
        if self.balance == 0:
            messagebox.showwarning("Withdraw", "Cannot withdraw from an empty account.")
        else:
            amount = simpledialog.askinteger("Withdraw", "Enter the amount to withdraw:")
            if amount is not None and 0 < amount <= self.balance:
                self.balance -= amount
                messagebox.showinfo("Withdraw", f"Amount withdrawn: ${amount}\nNew Balance: ${self.balance}")
                self.main_menu_page()
            else:
                messagebox.showerror("Withdraw", "Invalid amount. Please try again.")

    def logout(self):
        self.login_page()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.root.mainloop()

# Run the banking system application
banking_system = BankingSystem()
banking_system.run()