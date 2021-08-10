#!/usr/bin/python3
import datetime
import os
import socket
import smtplib

sender = 'openvpn@yourserver.com'
receivers = ['youremail@yourserver.com']

time = datetime.datetime.now()
formatted_time = time.strftime("%A, %B %d, %Y at %I:%M:%S %p")

message = """From: openvpn@yourserver.com
To: youremail@yourserver.com
MIME-Version: 1.0
Content-type: text/html
Subject: OpenVPN client connected

<b>OpenVPN client connected</b>
<h1>""" + formatted_time + """</h1>
"""

try:
   smtpObj = smtplib.SMTP('IP ADDRESS MAIL SERVER')
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")

