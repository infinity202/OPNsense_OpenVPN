#!/usr/bin/python3
import datetime
import os
import socket
import smtplib

sender = 'yoursendingaddress@server.info'
receivers = ['youradmin@server.info']

time = datetime.datetime.now()
formatted_time = time.strftime("%A, %B %d, %Y at %I:%M:%S %p")
#name = os.environ['common_name']
#localip = os.environ['ifconfig_pool_remote_ip']
#remoteip = os.environ['untrusted_ip']
#hostname = socket.getfqdn(remoteip)

message = """From: OPNSense <yoursendingaddress@server.info>
To: To Admin <youradmin@server.info>
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

