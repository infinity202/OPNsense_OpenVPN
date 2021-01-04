# OPNsense OpenVPN

After digging around in the OPNSense files I ended up with a solution that works. (period)
What we can do:
1. send an email via the installed python to a receiver and via a remote mail server as soon as a new client connects to our OpenVPN server

What we can't do: 
1. see who connected
2. see from where it connected
3. see more than the above 

It's a poor man's solution, but anyways it is more then we had before this exercise. So we must be proud and can rewards ourselfs with a beer after implementing this solution. 

This "solution" is not installable, comes with zero (0) or less warranty and may be distributed to anyone you know or don't know. 

This solution needs us to override a write protection on a certain file, so we are pushing limits. 

Since I couldn't find any traces of sendmail, mailx or other mail programs that can be run from the commandline I went to a python solution. 
This means we go from shebang - to shebang - to python. Is it ugly? Yeah! 

The solution:
1. A standard OpenVPN server config can be extended with a simple extra line saying "client-connect /my_badd_ass_script"
2. The good guys from OPNSense already use this solution and they seem to hide the line somewhere. 
3. Anyways, we can't use this
4. But we can find the standard script they (OPNsense) use and it is here 
  /usr/local/libexec/openvpn-client.up
5. We will break as little as we can so we will just add 1 extra line. At the end, just before "exit 0" and after the "fi"
6. We will write "/var/etc/up.sh" , which will be our new and extra script
7. Saving the file will result in a write warning, override this warning with w! 
8. So now we can create our new script located at /var/etc/  (see the file in this repo) (make sure you make it executable "chmod +x up.sh")
9. Now as you will see we will call a python script with the name client-up-extra.py
10. This file should also be created in /var/etc (make sure you make it executable "chmod +x client-up-extra.py")
11. See attached example. Make sure to adjust the mail server and sender and receiver addresses.
12. You don't have to restart any server or service since OpenVPN already knows it needs to call the script mentioned at 4. so everything will work fine instantly
