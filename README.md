# DemoQA Automation Project
This project contains automated tests for the DemoQA website using Python, Selenium WebDriver, and Behave (Cucumber for Python).

## Setup
1. Install Python 3.x from https://www.python.org/downloads/
2. Install required packages:
    pip install selenium behave webdriver-manager allure-behave
    pip install selenium behave webdriver-manager allure-behave pytest
3. Install Allure command-line tool:
- For Windows: `scoop install allure`
- For macOS: `brew install allure`

## Execution Procedure
1. Open a terminal in the project root directory.
2. Run `behave` to execute all tests, or specify a feature file to run individual tests.
3. After test execution, generate and view Allure reports using the commands mentioned above.
Each module can be executed separately by running its corresponding feature file. Make sure to have all dependencies installed and the WebDriver set up correctly before running the tests.

## Running Tests
To run all tests:
behave

To run a specific feature:
behave features/1_practice_form.feature

To run unit tests with pytest:
python -m pytest tests/test_browser_windows.py

To generate Allure reports:
behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure serve allure-results

## Module Explanations

### 1. Practice Form (1_practice_form.py)
This module automates filling out a practice form on the DemoQA website. It reads data from a text file, fills the form, submits it, and verifies that a confirmation popup appears.

### 2. Browser Windows (2_browser_windows.py)
This module tests the functionality of opening a new browser window. It navigates to the Browser Windows page, opens a new window, verifies its content, and then closes it.

### 3. Web Tables (3_web_tables.py)
This module demonstrates interaction with web tables. It creates a new record, edits it, and then deletes it, showcasing basic CRUD operations.

### 4. Web Tables - 12 Records (web_tables_steps.py)
This module extends the Web Tables functionality by creating 12 records dynamically and then deleting them all, demonstrating bulk operations.

### 5. Progress Bar (5_progress_bar.py)
This module tests a progress bar widget. It starts the progress, stops it before 25%, validates the progress value, then completes and resets the progress bar.

### 6. Sortable (6_sortable.py)
This module tests drag-and-drop functionality by sorting a list of items in ascending order.

## Project Structure
project/
│
├── features/
│ ├── steps/
│ │ └── common_steps.py
│ ├── 1_practice_form.feature
│ ├── 2_browser_windows.feature
│ ├── 3_web_tables.feature
│ ├── web_tables.feature
│ ├── 5_progress_bar.feature
│ └── 6_sortable.feature
│
├── pages/
│ ├── practice_form_page.py
│ ├── browser_windows_page.py
│ ├── web_tables_page.py
│ ├── progress_bar_page.py
│ └── sortable_page.py
│
├── tests/
│ ├── test_practice_form.py
│ ├── test_browser_windows.py
│ ├── test_web_tables.py
│ ├── test_web_tables_12.py
│ ├── test_progress_bar.py
│ └── test_sortable.py
│
├── utils/
│ └── driver_factory.py
│
├── data/
│ └── form_data.txt
│
├── environment.py
├── behave.ini
└── README.md