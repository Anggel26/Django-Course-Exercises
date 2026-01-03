# Django Course Exercises

This repository documents my progress in learning Django from scratch. I will be updating this README and adding new projects as I learn new concepts and move forward with the course.

> **Note:** Currently focusing on **URLs, Views, and HTTP Responses**. No Database (SQL) or Models have been implemented yet.

## 📑 Index

1. [Project Overview](#-project-overview)
2. [Detailed Concepts](#-detailed-concepts)
3. [How to Run](#-how-to-run)

---

## 📂 Project Overview

| Project | Key Concepts | Status |
| :--- | :--- | :--- |
| **[01-first-project](./01-first-project)** | Setup, File Structure, `django-admin` | ✅ Completed |
| **[02-monthly-challenges](./02-monthly-challenges)** | Dynamic URLs, Views, Path Converters, Redirects | ✅ Completed |
| *03-upcoming...* | *TBA* | 🚧 Pending |

---

## 🧠 Detailed Concepts

### 01-first-project
* **Goal:** Setting up the environment and understanding Django's boilerplate.
* **Tech:** Installation, `settings.py`, `manage.py`, launching the local server (`runserver`).

### 02-monthly-challenges
* **Goal:** Handling requests/responses and building a logic-based navigation.
* **Tech:**
    * **Dynamic Routes:** Flexible URL patterns (e.g., `/challenges/<month>`).
    * **Type Validation:** Distinguishing between integers and strings in the URL to trigger different behaviors (Redirects vs Rendering).
    * **Views:** Generating simple HTML content directly within Python functions.

---

## 🚀 How to Run

Since each folder is a standalone project, make sure to navigate to the correct directory before running the server.

1.  **Clone the repository.**
2.  **Navigate to the project folder** you want to run (e.g., `02-monthly-challenges`):
    ```bash
    cd 02-monthly-challenges
    ```
3.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```
4.  **Open your browser** at `http://127.0.0.1:8000/`.