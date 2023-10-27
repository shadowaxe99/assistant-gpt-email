
import unittest
from src.response_generator import generate_responses
from unittest.mock import patch, MagicMock

class TestResponseGenerator(unittest.TestCase):
    @patch('src.response_generator.ChatGPT')
    def test_generate_responses(self, mock_chatgpt):
        mock_chatgpt.generate_response = MagicMock(return_value="Test response")
        emails = [{"subject": "Test", "body": "This is a test email"}]
        responses = generate_responses(emails)
        self.assertEqual(len(responses), len(emails))
        self.assertEqual(responses[0]['response'], "Test response")

if __name__ == '__main__':
    unittest.main()
