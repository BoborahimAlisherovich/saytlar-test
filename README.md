# Vulnerability Scanner

Vulnerability Scanner is a Django-based web application that scans websites for common vulnerabilities such as Cross-Site Scripting (XSS) and SQL Injection.

## Features

- Scan websites for XSS and SQL Injection vulnerabilities.
- Display detected vulnerabilities in a user-friendly interface.
- Simple and easy to use.

## Installation


2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Open your web browser and navigate to:**

    ```
    http://127.0.0.1:8000/
    ```

## Usage

1. Enter the URL of the website you want to scan in the input field.
2. Click the "Scan" button.
3. If vulnerabilities are found, they will be displayed on the screen. If no vulnerabilities are found, a success message will be shown.

## Vulnerability Checks

The application currently checks for the following vulnerabilities:

- **Cross-Site Scripting (XSS):**
  - The application sends a script payload to the URL and checks if the payload is reflected in the response.

- **SQL Injection:**
  - The application sends an SQL injection payload to the URL and checks for syntax or error messages in the response.

## Adding More Vulnerability Checks

To add more vulnerability checks, you can modify the `scanner/scanner.py` file. Add your custom check functions and update the `scan_vulnerabilities` function to include your new checks.

Example:

```python
import requests

def check_xss(url):
    payload = "<script>alert('XSS')</script>"
    try:
        response = requests.get(url, params={'q': payload}, timeout=5)
        if payload in response.text:
            return "Potential XSS vulnerability found!"
    except requests.exceptions.RequestException:
        return None
    return None

def check_sql_injection(url):
    payload = "' OR '1'='1"
    try:
        response = requests.get(url, params={'id': payload}, timeout=5)
        if "syntax" in response.text or "error" in response.text:
            return "Potential SQL Injection vulnerability found!"
    except requests.exceptions.RequestException:
        return None
    return None

def scan_vulnerabilities(url):
    vulnerabilities = []
    xss_result = check_xss(url)
    if xss_result:
        vulnerabilities.append(xss_result)
    
    sql_result = check_sql_injection(url)
    if sql_result:
        vulnerabilities.append(sql_result)

    # Add more checks as needed

    return vulnerabilities
```   


Testing
The application includes basic tests for the vulnerability checks. To run the tests, use the following command:

```bash
python manage.py test scanner
```


Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For additional information or to report issues, you can contact:

Email: solihahusniddinova27@gmail.com
GitHub: Salikha003
