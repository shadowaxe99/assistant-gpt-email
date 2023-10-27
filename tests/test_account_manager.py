
import unittest
from src.account_manager import manage_new_email_account

class TestAccountManager(unittest.TestCase):

    def setUp(self):
        self.account_manager = manage_new_email_account()

    def test_account_creation(self):
        result = self.account_manager.create_account('test@gmail.com', 'password123')
        self.assertEqual(result, 'Account created successfully')

    def test_account_deletion(self):
        result = self.account_manager.delete_account('test@gmail.com')
        self.assertEqual(result, 'Account deleted successfully')

    def test_account_update(self):
        result = self.account_manager.update_account('test@gmail.com', 'newpassword123')
        self.assertEqual(result, 'Account updated successfully')

if __name__ == '__main__':
    unittest.main()
