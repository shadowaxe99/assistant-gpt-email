
import base64
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials

class DraftManager:
    def __init__(self, credentials):
        self.service = build('gmail', 'v1', credentials=credentials)

    def create_draft(self, user_id, message_body):
        try:
            message = {'raw': base64.urlsafe_b64encode(message_body.encode('UTF-8')).decode('ascii')}
            draft = self.service.users().drafts().create(userId=user_id, body=message).execute()
            return draft
        except HttpError as error:
            print(f'An error occurred: {error}')

if __name__ == "__main__":
    creds = Credentials.from_authorized_user_file('token.json')
    draft_manager = DraftManager(creds)
    draft_manager.create_draft('me', 'Hello, this is a test draft.')
