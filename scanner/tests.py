from django.test import TestCase
from .scanner import check_xss, check_sql_injection

class ScannerTests(TestCase):
    def test_check_xss(self):
        url = "http://example.com"
        result = check_xss(url)
        if result:
            self.assertIn("Potential XSS vulnerability", result)

    def test_check_sql_injection(self):
        url = "http://example.com"
        result = check_sql_injection(url)
        if result:
            self.assertIn("Potential SQL Injection vulnerability", result)

