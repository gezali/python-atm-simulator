<div align="center">

# 🏦 Simple Bank

### A clean, beginner-friendly banking app with a GUI, built with Python and Tkinter

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/license-MIT-blue)

<img src="Screenshot 2026-10-28 114939.png" alt="Simple Bank dashboard" width="380">

</div>

---

## ✨ Overview

**Simple Bank** is a desktop banking simulator. Create an account, get a randomly generated 15-character account number, log in securely with a PIN, and manage your money through a simple, friendly interface: deposit, withdraw, and watch your balance update in real time.

It uses only Python's standard library, so there is **nothing to install**.

## 🚀 Features

- 📝 **Account creation** with name, age, address, and a custom PIN
- 🔞 **Age verification**: only users 18 or older can open an account, and under-age users are told how many years they must wait
- 🔢 **Random account numbers**: unique 15-character alphanumeric IDs (A-Z, 0-9)
- 🔐 **PIN-protected login** with a 3-attempt limit; the account locks after too many wrong tries
- 💰 **Deposit and withdraw** with a live-updating balance in ₹
- 🛡️ **Input validation**: handles empty fields, non-numeric input, negative amounts, and insufficient balance
- ⌨️ **Press Enter to log in** for a smoother experience

## 📸 Screenshots

| Create Account | Account Created |
|:---:|:---:|
| <img src="Screenshot 2026-10-28 114903.png" width="300"> | <img src="Screenshot 2026-10-28 114915.png" width="300"> |

| PIN Login | Dashboard |
|:---:|:---:|
| <img src="Screenshot 2026-10-28 114928.png" width="300"> | <img src="Screenshot 2026-10-28 114939.png" width="300"> |

| Deposit | Withdraw |
|:---:|:---:|
| <img src="Screenshot 2026-10-28 114958.png" width="300"> | <img src="Screenshot 2026-10-28 115014.png" width="300"> |

## 🛠️ Getting Started

### Prerequisites

- **Python 3.8 or higher**
- **Tkinter**, which comes bundled with Python on Windows and macOS.
  On some Linux distributions you may need to install it:
  ```bash
  sudo apt install python3-tk
  ```

### Installation and run

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git

# 2. Move into the project folder
cd <your-repo-name>

# 3. Run the app
python main.py
```

> 💡 Replace `main.py` with the actual name of your Python file.

## 🧭 How to Use

1. **Create Account**: enter your name, age (18+), address, and a 4 to 6 digit PIN.
2. **Review Details**: check your account summary and note your account number.
3. **Login**: enter your PIN. You get 3 attempts before the account locks.
4. **Dashboard**: type an amount, then click **Deposit** or **Withdraw**.
5. **Exit**: click **Exit** when you are done.

## 🗂️ Project Structure

```
.
├── main.py              # Application code
├── README.md
└── screenshots/         # Images used in this README
    ├── 01-create-account.png
    ├── 02-account-created.png
    ├── 03-pin-login.png
    ├── 04-dashboard.png
    ├── 05-deposit.png
    └── 06-withdraw.png
```

## 🧩 How It Works

The app is a single `BankApp` class that extends `tk.Tk` and switches between four screens by clearing and redrawing one container frame:

| Screen | Method | Purpose |
|---|---|---|
| Create Account | `show_create_account()` | Collects and validates user details |
| Account Summary | `show_account_summary()` | Displays the new account info |
| PIN Login | `show_login()` | Verifies the PIN with limited attempts |
| Dashboard | `show_dashboard()` | Deposit, withdraw, and balance display |

## ⚠️ Note

This is a **learning project**. Data is stored in memory only and is lost when the app closes. The PIN is held as plain text, so it is not intended for real financial use.

## 🔮 Future Improvements

- [ ] Save accounts to a file or database (JSON / SQLite)
- [ ] Support multiple accounts and a registration/login system
- [ ] Add a transaction history view
- [ ] Hash PINs instead of storing them as plain text
- [ ] Add a "Change PIN" option
- [ ] Dark mode theme

## 🤝 Contributing

Suggestions and pull requests are welcome. Fork the repo, create a branch, and open a PR.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ and Python

⭐ If you found this helpful, consider giving the repo a star!

</div>
