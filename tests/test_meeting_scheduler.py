
import unittest
from src.meeting_scheduler import schedule_zoom_meeting
from unittest.mock import patch

class TestMeetingScheduler(unittest.TestCase):

    @patch('src.meeting_scheduler.ZoomAPI')
    def test_schedule_zoom_meeting(self, MockZoomAPI):
        # Arrange
        mock_api = MockZoomAPI()
        mock_api.schedule_meeting.return_value = {"meeting_id": "123456"}

        # Act
        result = schedule_zoom_meeting(mock_api, "test@gmail.com", "Test Meeting", "2022-12-31 10:00:00")

        # Assert
        self.assertEqual(result, {"meeting_id": "123456"})
        mock_api.schedule_meeting.assert_called_once_with("test@gmail.com", "Test Meeting", "2022-12-31 10:00:00")

if __name__ == '__main__':
    unittest.main()

