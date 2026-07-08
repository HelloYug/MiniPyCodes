# 📌 Excel To MySQL

### 📁 Folder: `Excel To MySQL`

This project is a Python script designed to extract data from an Excel sheet and insert it into a MySQL database. It is ideal for automating the process of transferring attendance or other tabular data from Excel into MySQL, simplifying the data management process.

## 📋 Features

- Extracts data from an Excel sheet.
- Inserts the data into a MySQL table.
- Supports replacing `None` values with `NULL` in MySQL for compatibility.


## 🛠 Requirements

- Python 3.6+
- Required libraries:
    ```bash
    pip install -r requirements.txt
    ```


## 🚀 Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/HelloYug/MiniPyCodes.git
   ```

2. Navigate to this folder:

   ```bash
   cd MiniPyCodes/Excel To MySQL
   ```

3. Run the script:

   ```bash
   python3 ExcelToMySQL.py
   ```

4. Usage sample - test_run.py
   ```
   from excel_to_mysql import run_import

   success = run_import(
      file_path="datasheets.xlsx",
      sheet_name="attendence",
      database_name="bni",
      table_name="attendence"
   )

   if success:
      print("Import successful.")
   else:
      print("Import failed.")
   ```


## 📎 Files
```
Excel To MySQL/
│
├── .env                    → DB Credentials Input
├── README.md               → Project documentation
├── ExcelToMySQL.py         → Main Python script (core logic)
├── requirements.txt        → Python package dependencies

```

---

## 📄 License

This project is licensed under the **MIT License**.

## 👨‍💻 Author

**Yug Agarwal**

* 📧 Email – [yugagarwal704@gmail.com](mailto:yugagarwal704@gmail.com)
* 🔗 GitHub – [@HelloYug](https://github.com/HelloYug)
* 💼 LinkedIn – [yugagarwal704](https://www.linkedin.com/in/yugagarwal704/)
* 🌐 Website – [yugagarwal.dev](https://yugagarwal.dev/?utm_source=github&utm_medium=readme&utm_campaign=Excel_To_MySQL_readme)
