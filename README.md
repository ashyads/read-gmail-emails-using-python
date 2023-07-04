# Gmail Email Processing Script

This script allows you to fetch and process emails from a Gmail account using the IMAP protocol. It uses the `imap_tools` library to interact with the Gmail IMAP server.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your system.
- The `imap_tools` library installed. You can install it using pip:


## Configuration

To use the script, you need to provide your Gmail credentials and adjust the filtering criteria for fetching emails. Follow these steps:

1. Open the script file (`main.py`) in a text editor.
2. Replace the `GMAIL_EMAIL` variable with your Gmail email address.
3. Replace the `GMAIL_PASSWORD_KEY` variable with your Gmail password or app password.

## Usage

To run the script, execute the following command in your terminal:

The script will log in to your Gmail account, fetch emails from the current date, and process them. The processed email details will be displayed in the console output.

## Customization

You can customize the script to suit your specific requirements. Here are some possible modifications:

- Adjust the `from_date` variable to fetch emails from a specific date or time range.
- Extend the processing logic to perform additional actions with the fetched emails, such as saving attachments or analyzing email content.

## Limitations

- This script currently supports Gmail accounts and uses the Gmail IMAP server (`imap.gmail.com`). If you're using a different email provider, you may need to modify the script accordingly.
- Ensure that your Gmail account has IMAP access enabled. You can check the Gmail settings to enable IMAP if needed.

## License

This script is released under the MIT License. Feel free to modify and use it according to your needs.

