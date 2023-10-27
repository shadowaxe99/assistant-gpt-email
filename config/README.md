# Auto Email Responder

This application monitors a Gmail inbox, fetches unread emails, generates automatic responses using ChatGPT, saves the responses as drafts, manages new email accounts, and schedules meetings using ZoomAPI.

## Features

- Fetch unread emails from a Gmail account
- Generate responses using ChatGPT
- Save generated responses as drafts
- Manage new email accounts
- Schedule meetings using ZoomAPI

## Installation

1. Clone the repository
2. Install the dependencies using `pip install -r requirements.txt`
3. Configure your Gmail, ChatGPT, and ZoomAPI credentials in `config/settings.py`
4. Run `main.py` to start the application

## Testing

Run `python -m unittest discover tests` to execute the tests.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)