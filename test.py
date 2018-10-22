"""The first step is to create an SMTP object, each object is used for connection 
with one server."""

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

#Next, log in to the server
server.login("secret.santa.mercutwright@gmail.com", "Longbow1")

#Send the mail
msg = "YOUR MESSAGE!"
server.sendmail("secret.santa.mercutwright@gmail.com", "alun.g.m@gmail.com", msg)
server.quit()