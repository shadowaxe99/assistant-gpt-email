
import json
from zoomus import ZoomClient

class MeetingScheduler:
    def __init__(self, api_key, api_secret):
        self.client = ZoomClient(api_key, api_secret)

    def schedule_meeting(self, user_id, meeting_topic, start_time, duration, timezone):
        response = self.client.meeting.create(
            user_id=user_id,
            topic=meeting_topic,
            start_time=start_time,
            duration=duration,
            timezone=timezone
        )
        return json.loads(response.content)

if __name__ == "__main__":
    scheduler = MeetingScheduler('your_api_key', 'your_api_secret')
    response = scheduler.schedule_meeting('user_id', 'Meeting Topic', '2022-01-01T10:00:00', 60, 'UTC')
    print(response)
