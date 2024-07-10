import smtplib
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText
from faker import Faker
from typing import List


def send_email(to_addrs: List[str], body):
    faker = Faker()
    from_addr = "bs6w2yi4gtyxpc2s@ethereal.email"
    login = "bs6w2yi4gtyxpc2s@ethereal.email"

    password = "E3h1j7wPbSfAYES22J"

    message = MIMEMultipart()
    message["From"] = faker.email()
    message["to"] = ", ".join(to_addrs)

    message["Subject"] = "Confirmação de viagem"
    message.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.ethereal.email", 587)

    server.starttls()
    server.login(login, password)

    text = message.as_string()

    for to_addr in to_addrs:
        server.sendmail(from_addr, to_addr, text)

    server.quit()
