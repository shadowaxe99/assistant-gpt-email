
import unittest
from src.email_manager import EmailManager

class TestEmailManager(unittest.TestCase):
    def setUp(self):
        self.email_manager = EmailManager()

    def test_fetch_unread_emails(self):
        emails = self.email_manager.fetch_unread_emails()
        self.assertIsInstance(emails, list)

    def test_mark_as_read(self):
        email_id = '123abc'
        result = self.email_manager.mark_as_read(email_id)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
