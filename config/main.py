
import os
from src.email_manager import EmailManager
from src.response_generator import ResponseGenerator
from src.draft_manager import DraftManager
from src.account_manager import AccountManager
from src.meeting_scheduler import MeetingScheduler

def main():
    email_manager = EmailManager()
    response_generator = ResponseGenerator()
    draft_manager = DraftManager()
    account_manager = AccountManager()
    meeting_scheduler = MeetingScheduler()

    # Fetch unread emails
    unread_emails = email_manager.fetch_unread_emails()

    for email in unread_emails:
        # Generate response
        response = response_generator.generate_responses(email)

        # Save response as draft
        draft_manager.save_drafts(response)

        # Manage new email account
        account_manager.manage_new_email_account(email)

        # Schedule meeting
        meeting_scheduler.schedule_zoom_meeting(email)

if __name__ == "__main__":
    main()
