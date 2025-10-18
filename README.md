# RR QA Automation Assignment

## Overview
This repository contains the automated UI + API test suite for TMDB Discover demo site, using Python, Selenium, PyTest, and Requests.

## Setup & Execution

1. Clone repository  
2. `pip install -r requirements.txt`  
3. Run tests: `pytest`  
4. Reports and logs generated under `reports/`, including timestamped HTML report

## Tools & Framework
- Selenium (UI automation)  
- Requests (API validation)  
- PyTest (test framework)  
- WebDriver Manager (auto ChromeDriver)  
- pytest-html (report generation)  
- Python logging, screenshot capture

## CI/CD (Jenkins)
A sample `Jenkinsfile` is included (to build, run tests, archive reports)

## Defects & Observations
Refer to `defects.md`

