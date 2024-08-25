import requests

def check_xss(url):
    # Example check for XSS vulnerability
    payload = "<script>alert('XSS')</script>"
    try:
        response = requests.get(url, params={'q': payload}, timeout=5)
        if payload in response.text:
            return "Potential XSS vulnerability found!"
    except requests.exceptions.RequestException:
        return None
    return None

def check_sql_injection(url):
    # Example check for SQL Injection vulnerability
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

