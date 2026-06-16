import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = "Привет из Python!"
msg['From'] = "test@yandex.ru"
msg['To'] = "redrepublics@yandex.ru"

msg.set_content("Это письмо создано при отладке, можете на него не отвечать.")
msg.add_alternative("<html><body>Привет!</body></html>", subtype="html")

# smtp.yandex.ru 465

with smtplib.SMTP_SSL('smtp.yandex.ru', 465) as smtp:
    smtp.login("redrepublics@yandex.ru", "pas")
    smtp.send_message(msg)

print('Успех')
#нужна отладка