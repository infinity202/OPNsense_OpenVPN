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
Subject: OpenVPN client disconnected
<b>OpenVPN client disconnected</b>
<h1>""" + formatted_time + """</h1>
"""

try:
   smtpObj = smtplib.SMTP('192.168.1.12')
# change the IP-address to your mail server address    
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")
