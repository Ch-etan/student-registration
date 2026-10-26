
from html.parser import HTMLParser
from pathlib import Path
import unittest


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.form_found = False
        self.submit_found = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form" and attrs.get("id") == "registrationForm":
            self.form_found = True

        if tag == "input":
            if attrs.get("id"):
                self.ids.add(attrs["id"])

        if tag == "select" and attrs.get("id"):
            self.ids.add(attrs["id"])

        if tag == "button" and attrs.get("type") == "submit":
            self.submit_found = True


class RegistrationFormTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        html = Path("index.html").read_text(encoding="utf-8")
        cls.parser = FormParser()
        cls.parser.feed(html)

    def test_form_exists(self):
        self.assertTrue(self.parser.form_found)

    def test_student_name_exists(self):
        self.assertIn("studentName", self.parser.ids)

    def test_roll_number_exists(self):
        self.assertIn("rollNumber", self.parser.ids)

    def test_email_exists(self):
        self.assertIn("email", self.parser.ids)

    def test_course_exists(self):
        self.assertIn("course", self.parser.ids)

    def test_submit_button_exists(self):
        self.assertTrue(self.parser.submit_found)


if __name__ == "__main__":
    unittest.main(verbosity=2)
