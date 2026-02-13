# 🚀 Python API Automation Framework

Hybrid Custom API Automation Framework built with a scalable and maintainable folder structure.
Designed for REST API testing with advanced reporting, parallel execution, and schema validation.

---

## 📌 Project Overview

This framework provides:

* Structured API test automation
* Parallel execution support
* Advanced reporting with Allure & HTML
* Test data management (CSV, Excel, JSON)
* JSON schema validation
* Faker-based dynamic data generation
* Clean and modular architecture


![Screenshot 2024-08-05 at 08 18 38](https://github.com/user-attachments/assets/3c7d5fe5-207a-42e7-84fe-f4d53354d987)


---

## 🏗️ Folder Structure

Below is the recommended project structure:

```
.
├── tests/
│   ├── crud/
│   ├── integration/
│   └── regression/
├── src/
│   ├── api/
│   ├── payloads/
│   ├── utilities/
│   └── config/
├── testdata/
│   ├── csv/
│   ├── excel/
│   └── json/
├── reports/
├── requirements.txt
└── pytest.ini
```

---

## 🛠️ Tech Stack

* **Python 3.12**
* **Requests** – HTTP client
* **PyTest** – Testing framework
* **Allure Report** – Advanced reporting
* **PyTest HTML** – HTML reporting
* **Faker** – Dynamic test data
* **jsonschema** – API schema validation
* **pytest-xdist** – Parallel execution
* **CSV / Excel / JSON** – Test data management

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-url>
cd <project-folder>
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install requests pytest pytest-html faker allure-pytest jsonschema pytest-xdist
```

---

## ▶️ Running Test Cases

### ✅ Run Basic Test

```bash
pytest
```

---

### ⚡ Run Tests in Parallel

```bash
pytest -n auto
```

Or specify number of threads:

```bash
pytest -n 4
```

---

### 📊 Generate Allure Report

Run tests with:

```bash
pytest tests/tests/crud/test_create_booking.py --alluredir=allure_result -s
```

Generate report:

```bash
allure serve allure_result
```

---

### 📝 Generate PyTest HTML Report

```bash
pytest --html=report.html
```

---

## 🔍 Advanced Features

✔ JSON Schema Validation
✔ Faker dynamic test data
✔ Data-driven testing (CSV, Excel, JSON)
✔ Parallel execution support
✔ Modular reusable API utilities
✔ Scalable folder structure
✔ Environment configuration support

---

## 🧪 Sample Test Execution Strategy

* Smoke Tests
* Regression Suite
* Integration Tests
* CRUD Operations
* Negative Testing
* Schema Validation
* Response Time Validation

---

## 📦 Recommended Improvements (Optional Enhancements)

You can further enhance this framework by adding:

* 🔐 Environment configuration (.env support)
* 🧾 Logging framework (Python logging)
* 🔄 CI/CD integration (GitHub Actions)
* 🐳 Docker support
* 📈 Performance testing using JMeter
* 🔍 Code linting (flake8, black)
* 📊 Coverage reports

---

## 🤝 Contribution Guidelines

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to your branch
5. Create a Pull Request

---

## 📚 Best Practices Followed

* Page Object like structure for APIs
* Reusable API request methods
* Clean separation of test logic & payloads
* Externalized test data
* Configurable environments
* Scalable architecture

---

## 👨‍💻 Author

**Harsh Sharma**
QA Automation Engineer | API Testing Specialist

If you like this project, ⭐ star the repository!

---

## 📄 License

This project is open-source and available under the MIT License.

---
