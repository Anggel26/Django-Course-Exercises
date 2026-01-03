# 02-monthly-challenges

[← Back to Main Repository](../README.md)

### 📌 About
A Django application that manages monthly challenges using dynamic URLs and View logic. The goal was to understand how Django routes requests without using a Database or Templates yet.

### ⚙️ Technical Highlights

#### 1. Dynamic URLs & Path Converters
We moved away from hardcoded paths.
* **String Path:** `challenges/<month>` captures the month name.
* **Integer Path:** `challenges/<int:month>` captures a number to handle redirects.

#### 2. View Logic (The "Brain")
* **Reverse Logic:** If the user enters a number (e.g., `/1`), the view converts it to "january" and redirects.
* **Validation:** Returns a `404` response if the month is invalid.
* **HTML Generation:** The HTML is currently constructed manually within the Python functions (e.g., string concatenation) to understand the underlying HTTP response structure.

### 🚦 How to Run this specific project
```bash
# Make sure you are inside this folder
python manage.py runserver
```

---
*Created as part of the Django Course Exercises.*
