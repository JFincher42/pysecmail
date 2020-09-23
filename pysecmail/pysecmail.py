"""PySecMail
Generate a secure temporary email address
Allows you to create, monitor, and delete the address at will
"""

import requests
import json


# API info
endpoint = "https://www.1secmail.com/api/v1/"
domain = "1secmail.com"


# Functions
def get_messages(email: str) -> list:
    """Gets all the messages for a given email address

    Args:
        email (str): which email address?

    Returns:
        list: A list of email messages. Each message is a dict of the form:
              { "id":      number,
                "from":    email address,
                "subject": free text,
                "date":    datetime }
    """

    params = {"action": "getMessages", "login": email, "domain": domain}

    response = requests.get(endpoint, data=params)
    email_data = json.load(response)

    for email_message in email_data:
        for field, value in email_message.items():
            print(f"{field}: {value}")
        print()