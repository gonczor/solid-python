from urllib import request
from json import loads

url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmanufacturerdetails/{make}?format=json"
fake_username = "someone@example.com"
fake_password = "secret"

class Contacts:
    """Collects emails from NHTSA database and sends emails to contacts"""
    def send_emails(self, make: str, message: str, username: str, password: str):
        data = self.download_data(make)
        emails = self.extract_emails(data)
        if self.login(username, password):
            for email in emails:
                self.send(username, email, message)
        else:
            print("Error logging in. Aborting!")

    def download_data(self, make: str) -> list:
        response = request.urlopen(url.format(make=make))
        return loads(response.read())["Results"]
    
    def extract_emails(self, data: list) -> list:
        return [
            element["ContactEmail"]
            for element in data
            if element["ContactEmail"] is not None
        ]
    
    def login(self, username: str, password: str) -> bool:
        print("Connecting to server...")
        print("Authorizing email account...")
        if username == "someone@example.com" and password == "secret":
            print("Access granted")
            return True
        else:
            print("Wrong credentials")
            return False

    def send(self, sender: str, receiver: str, message: str):
        print()
        print("=" * 10)
        print()
        print(f"From: {sender}")
        print(f"To: {receiver}")
        print(f"Body: {message}")
        print()
        print("=" * 10)
        print()


if __name__ == "__main__":
    make = input("Give make: ")
    message = input("Give message: ")
    contacts = Contacts()
    contacts.send_emails(make, message, fake_username, fake_password)

