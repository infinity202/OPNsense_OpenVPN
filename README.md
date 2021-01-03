# OPNsense OpenVPN
Additional script for automaticly sending emails when a OpenVPN client connects to the OpenVPNserver. 

This can be used as an alert when an unexpected connection is made to your OpenVPN server. 

After making all scripts and modifications you must disable and enable the OpenVPN server so it will re-read the config file

Don't forget to chmod +x the 2 files up.sh and client-up-extra.py

The first OpenVPN server has config file /var/etc/openvpn/server1.conf, second will have server2.conf
