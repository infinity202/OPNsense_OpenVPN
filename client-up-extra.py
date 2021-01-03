#!/usr/bin/python3
import datetime
import os
import socket
import smtplib

sender = 'openvpn@yourdomain.com'
receivers = ['admin@yourdomain.com']

time = datetime.datetime.now()
formatted_time = time.strftime("%A, %B %d, %Y at %I:%M:%S %p")

message = """From: OPNSense <opnsense@yourdomain.com>
To: To Admin <admin@yourdomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: OpenVPN client connected

OpenVPN client connected

<b>OpenVPN client connected</b>
<h1>""" + formatted_time + """</h1>
"""

try:
   smtpObj = smtplib.SMTP('yourmailserver.com')
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")

## Don't forget to set all email addresses and you need to use an external mailserver at line 26
