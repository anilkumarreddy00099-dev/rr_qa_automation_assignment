# TMDB UI & API Automation Assignment

This project is an automated test suite designed to validate the UI and basic API flows of the [TMDB Demo Site](https://tmdb-discover.surge.sh/).  
The solution follows a PyTest + Selenium Page Object Model (POM) structure with reporting and logging.

---

## Project Structure
```
rr_qa_automation_assignment/
│── pages/
│ └── home_page.py # Page Object file for Home Page actions
│── tests/
│ └── test_tmdb_ui_api.py # PyTest test cases
│── utils/
│ └── logger.py # Centralized logger
│── conftest.py # WebDriver setup
│── pytest.ini # PyTest configuration
│── requirements.txt # Dependencies
│── reports/ # HTML test reports
│── README.md # Project documentation
```

---

## Tools & Libraries
- Python 3.10+
- PyTest
- Selenium WebDriver
- PyTest-HTML
- Requests
- Logging

---

## Features Automated
- Category filtering: Popular, Trend, Newest, Top Rated
- Movie Type selection (React dropdown)
- Pagination (Page 2)
- Invalid slug negative scenario
- Sample API validation
- HTML reporting with logs

---

## Install Dependencies
```pip install -r requirements.txt```

---
## Run all test Suite
```pytest```

---
## Run with HTML report:
```pytest --html=reports/report.html --self-contained-html```

