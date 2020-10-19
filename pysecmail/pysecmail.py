"""PySecMail
Generate a secure temporary email address
Allows you to create, monitor, and delete the address at will
"""

# Imports
import requests  # To make Web API calls
import json  # To store and retrieve data
import sys  # Access to argv
import pathlib  # Path referencing the right way

from PyQt5.QtWidgets import *  # To manipulate the window
from PyQt5.QtCore import *  # For core QT functionality
from PyQt5.QtGui import *  # Gui elements

from MainWindow import Ui_MainWindow  # My main window


# API info - may be expanded later
endpoint = "https://www.1secmail.com/api/v1/"
domain = "1secmail.com"

# Some data from the provider
email_domains = [
    "1secmail.com",
    "1secmail.org",
    "1secmail.net",
    "wwjmp.com",
    "esiix.com",
]


# Configuration info
class ConfigData:
    def __init__(self):
        self.config_filename = (
            pathlib.Path(".") / "pysecmail" / "pysecmail.json"
        )

        self.config_data = dict()
        if self.config_filename.exists():
            # Read that file
            with open(self.config_filename, "r") as config_file:
                self.config_data = json.load(config_file)

    def get_email_addresses(self):
        return self.config_data.keys()

    def get_email_config_file(self, email_address):
        return self.config_data[email_address]


# QT Main Window
class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window for the application

    Args:
        QMainWindow ([type]): QT Main Window
        UI_MainWindow ([type]): My designed main window
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Setup some basics here
        self.cboDomain.addItems(email_domains)
        self.email_data = ConfigData()

        self.modelEmailAddresses = QStringListModel(
            self.email_data.get_email_addresses()
        )
        self.lstEmailAddresses.setModel(self.modelEmailAddresses)


# Functions
def generate_email_address(count: int = 1) -> list:
    """Generate one or more email
    addresses to use

    Args:
        count (int): How many email addresses to create (default 1)

    Returns:
        list: A list of email addresses
    """

    pass


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


# Main entry point
if __name__ == "__main__":

    # The one and only QT App
    app = QApplication(sys.argv)

    # The main window
    window = MainWindow()
    window.show()
    app.exec()
