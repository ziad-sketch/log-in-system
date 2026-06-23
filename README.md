# 🔐 Login System (Python Project)

## 📌 Overview
This is a simple command-line Login System built using Python.  
It allows users to create accounts, view accounts, search for users, and log in.  
All data is stored using a JSON file so accounts remain saved after closing the program.

---

## 🚀 Features
- Create new user accounts (username + password)
- View all saved accounts
- Search for a specific account
- User login authentication
- Prevent duplicate usernames
- Prevent empty username or password
- Automatic saving using JSON

---

## 🛠️ Technologies Used
- Python 🐍
- JSON (for data storage)

---

## 📂 How It Works
User accounts are stored in a dictionary format:

```python
{
  "Ahmed": "1234",
  "Sara": "pass123"
}
```

- Key → Username  
- Value → Password  

---

## ▶️ How to Run
1. Make sure Python is installed
2. Download the project files
3. Run the program:

```bash
python main.py
```

---

## 📋 Menu Options
```
1 Add account
2 View accounts
3 Search account
4 Login
5 Exit
```

---

## 💡 Example Usage
```
Choose option: 1
Enter username: Ahmed
Enter password: 1234
account saved successfully
```

---

## 🔑 Login Example
```
log in username: Ahmed
Enter password: 1234
log in successfully
```

---

## ⚠️ Notes
- Data is stored in `accounts.json`
- Passwords are stored in plain text (for learning purposes only)
- Make sure not to delete the JSON file if you want to keep accounts

---

## 📈 Future Improvements
- Encrypt passwords (hashing with bcrypt)
- Add password strength checker
- Add "forgot password" feature
- Add GUI version (Tkinter)
- Add email or phone verification

---

## 👨‍💻 Author
Beginner Python Project – built for learning and portfolio practice
