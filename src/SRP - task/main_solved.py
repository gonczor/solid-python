from urllib import request
from json import loads

url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmanufacturerdetails/{make}?format=json"
fake_username = "someone@example.com"
fake_password = "secret"

class EmailExtractor:
    def __init__(self, make: str):
        self.make = make

    def get_contacts(self) -> list:
        data = self._download_data()
        return self._extract_emails(data)
        
    def _download_data(self) -> list:
        response = request.urlopen(url.format(make=self.make))
        return loads(response.read())["Results"]
    
    def _extract_emails(self, data: list) -> list:
        return [
            element["ContactEmail"]
            for element in data
            if element["ContactEmail"] is not None
        ]

class EmailSender:
    def __init__(self, username: str, password: str, contacts: list, message: str):
        self._username = username
        self._password = password
        self._contacts = contacts
        self._message = message

    def send(self):
        if self._login():
            for contact in self._contacts:
                self._send(contact)
        else:
            print("Error logging in. Aborting!")

    def _login(self) -> bool:
        print("Connecting to server...")
        print("Authorizing email account...")
        if self._username == "someone@example.com" and self._password == "secret":
            print("Access granted")
            return True
        else:
            print("Wrong credentials")
            return False

    def _send(self, receiver: str):
        print()
        print("=" * 10)
        print()
        print(f"From: {self._username}")
        print(f"To: {receiver}")
        print(f"Body: {self._message}")
        print()
        print("=" * 10)
        print()


if __name__ == "__main__":
    make = input("Give make: ")
    message = input("Give message: ")
    extractor = EmailExtractor(make)
    contacts = extractor.get_contacts()
    sender = EmailSender(fake_username, fake_password, contacts, message)
    sender.send()

