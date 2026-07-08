# HandyPy 🛠️
A lightweight Python utility toolkit with reusable functions for formatting, math, encryption, validation, system tools, and more.

---

## 📦 Modules

### 🔣 Formatters (`handypy/formatters.py`)
- `AniType`: Typewriter-style printing effect
- `FormatNum`: Pad numbers with leading zeros
- `DeciFormatNum`: Format decimals with fixed lengths
- `DeciIntFormatter`: Convert floats like 3.0 to 3
- `GetInitials`: Get initials from full name
- `StringListAD`: Split on alphabet-digit transitions
- `StringListAll`: Split on all character type changes
- `shuffle_data`: Randomly shuffle string, list, tuple, or dictionary

### 🧮 Math Utilities (`handypy/math_utils.py`)
- `GCD`: Get GCD and factors of a number list
- `LCM`: Get LCM and multiples of a number list
- `DecimalToFraction`: Convert decimal to fraction string
- `DeciRange`: Float-compatible range()

### 💰 Financial Tools (`handypy/financial_tools.py`)
- `SuccessiveDiscount`: Apply chained percentage discounts

### 🔐 Crypto Utils (`handypy/crypto_utils.py`)
- `CharNum`, `NumChar`: Convert words ↔ numeric series
- `NumEncryption`, `NumDecryption`: Encrypt/decrypt integers
- `Encryption`, `Decryption`: Scramble and restore full strings

### 🖥️ System Tools (`handypy/system_tools.py`)
- `remove_blank_lines`: Remove blank lines from text file
- `find_window_by_title`: Switch to a window via title (Windows only)

### 🧪 Validators (`handypy/validators.py`)
- `InputData`: Type-safe input with retry loop

### 🗂️ Directory Utilities (handypy/directory_utilities.py)
- **A menu-driven directory management utility with:**

    - `generate_directory_chart`: Create a Markdown tree chart with file sizes (auto-formatted in B, KB, MB) and chart generation timestamp. Marks excluded files as [Excluded].

    - `copy_files_only`: Recursively copy only files (no folders) to a flat destination folder, skipping files with specified extensions and safely renaming duplicates.

    - `create_blank_structure`: Recreate the folder-file structure in a destination with empty files, useful for scaffolding or template generation.
---

## 🧰 Installation

```bash
git clone https://github.com/helloyug/handypy.git
cd handypy
pip install -r requirements.txt
````

---

## 🧪 Usage Example

```python
from handypy.formatters import AniType
from handypy.crypto_utils import Encryption, Decryption
from handypy.math_utils import DecimalToFraction

AniType("Hello World\n")
print(Encryption("Secret Message"))
print(DecimalToFraction(2.5))
```

---

## ⚠️ OS Compatibility

* `find_window_by_title` requires **Windows** with `pyautogui` and `pywin32`
* Most other functions are cross-platform and Python 3.7+

---

## 📝 License

MIT License. Free for personal and commercial use. Attribution appreciated.

---

## 👨‍💻 Author

**Yug Agarwal**

* 📧 Email – [yugagarwal704@gmail.com](mailto:yugagarwal704@gmail.com)
* 🔗 GitHub – [@HelloYug](https://github.com/HelloYug)
* 💼 LinkedIn – [yugagarwal704](https://www.linkedin.com/in/yugagarwal704/)
* 🌐 Portfolio – [yugagarwal.dev](https://yugagarwal.dev/?utm_source=github&utm_medium=readme&utm_campaign=MiniPyCodes_readme)