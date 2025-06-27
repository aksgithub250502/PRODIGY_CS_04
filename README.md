# 🧩 Simple Keylogger (Python)

## 📌 Task 04 – Prodigy InfoTech Cyber Security Internship

This is a basic yet enhanced **keylogger** developed using Python. It captures and logs keystrokes made by the user and saves them to a timestamped log file. This project is built for educational purposes only and highlights the ethical considerations involved in cybersecurity practices.

---

## ✅ Features

- Logs all keyboard input.
- Uses hotkeys to **start (`F9`)**, **stop (`F10`)**, and **exit (`ESC`)**.
- Saves keystrokes in a human-readable format.
- Auto-generates a new log file with a timestamp.
- Terminal/console feedback while logging.

---

## ⚙️ How It Works

1. The script listens for all keyboard events using the `pynput` library.
2. Pressing `F9` activates keylogging.
3. While active, every key pressed is recorded in a text file.
4. Pressing `F10` stops the logging temporarily.
5. Pressing `ESC` exits the program entirely.
6. Logs are saved in the format:
```

keylog\_YYYY-MM-DD\_HH-MM-SS.txt

```
## 🛠 Installation
### 1. Clone the Repository or Download the File
```bash
git clone https://github.com/aksgithub250502/PRODIGY_CS_04.git
```

---

### 2. Install Required Python Library

```bash
pip install pynput
```

---

## ▶️ How to Use
1. Open your terminal and navigate to the project directory:

```bash
   cd PRODIGY_CS_04
```

2. Run the script:

```bash
   python enhanced_keylogger.py
```

3. **Control Keys**:

   * `F9` → Start logging
   * `F10` → Stop logging
   * `ESC` → Exit the keylogger

4. **Log Output**: A new `.txt` file will be created in the same folder with all recorded keystrokes.

---
## 📸 Screenshots
> ![Simple Keylogger Program](https://github.com/user-attachments/assets/017d4d83-c529-4cb0-98b0-401eb3803a46)

> ![Simple Keylogger Output](https://github.com/user-attachments/assets/0f86936b-9a37-4ea4-bd9b-e73f3b28bc13)

---
## 📁 Folder Structure

```
PRODIGY_CS_04/
├── enhanced_keylogger.py      # Main Python script
├── keylog_YYYY-MM-DD_*.txt    # Generated key logs
└── README.md                  # Project documentation

```

---

## ⚠️ Ethical Consideration

> **Disclaimer**: This keylogger is intended for learning and demonstration purposes **only**. Do **not** use this software on any machine without **informed consent**. Unauthorized use of keyloggers is unethical and may be **illegal** under cybersecurity laws.

---

## 👨‍💻 Author
**AMAN KUMAR SINGH**
* Cyber Security Intern – Prodigy InfoTech
* GitHub: [@aksgithub250502]**(https://github.com/aksgithub250502/)**
* Email - [aman.aks1402@gmail.com]

## 📄 License

This project is developed under the **Cyber Security Internship** program by **Prodigy InfoTech**.
It is intended solely for **educational and learning purposes**.

---
## ✅Internship Task 04 Completed
This project fulfills **Task 04: Simple Keylogger** of the **Prodigy InfoTech Cyber Security Internship**.
