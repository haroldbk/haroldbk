#loop over rows to send multiple Emails
#https://realpython.com/python-send-email/

import csv, smtplib,ssl

message = """Subject: Your grade

Hi {name}, your grade is {grade}"""
from_address = "haroldbk@estatesway.org"
from_address =  "haroldbk@estatesway.org"
password = input("type your password then press enter:")
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.ionos.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("emaillist.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, grade in reader:
            server.sendmail(
                from_address,
                email,
                message.format(name=name,grade=grade),
            )
     

