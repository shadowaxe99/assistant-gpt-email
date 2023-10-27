
import unittest
from src.draft_manager import save_drafts

class TestDraftManager(unittest.TestCase):
    def setUp(self):
        self.draft_manager = save_drafts()

    def test_save_drafts(self):
        self.assertEqual(self.draft_manager.save_drafts("test@gmail.com", "Test Subject", "Test Body"), "Draft saved successfully")

    def test_save_drafts_no_subject(self):
        self.assertEqual(self.draft_manager.save_drafts("test@gmail.com", "", "Test Body"), "Subject is required")

    def test_save_drafts_no_body(self):
        self.assertEqual(self.draft_manager.save_drafts("test@gmail.com", "Test Subject", ""), "Body is required")

    def test_save_drafts_no_recipient(self):
        self.assertEqual(self.draft_manager.save_drafts("", "Test Subject", "Test Body"), "Recipient is required")

if __name__ == '__main__':
    unittest.main()
