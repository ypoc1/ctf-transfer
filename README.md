# ctf-transfer
Global Transfer Command for CTF's

This tool helps you transfer files between machines by using a simple Python HTTP server and various download commands (certutil, iwr, wget, curl).

## Features
- Easy setup of an HTTP server to share files.
- Generates commands for multiple download methods.
- Automatically zips directories before transfer.
- Copies the certutil command to the clipboard for easy use.

##USAGE

transfer $File
transfer $Folder

#Example
```
transfer hosts.txt     
Available network interfaces:
1: lo
2: eth0
3: eth1
Choose an interface by number:
Certutil command: certutil -urlcache -split -f "http://192.168.1.60/hosts.txt" hosts.txt
IWR command: iwr -Uri "http://192.168.1.60/hosts.txt" -OutFile "hosts.txt"
Wget command: wget http://192.168.1.60/hosts.txt
Curl command: curl -O http://192.168.1.60/hosts.txt
Certutil command copied to clipboard!
Starting Python HTTP server on 192.168.1.60:80
Press Ctrl+C to stop the server.
Serving HTTP on 192.168.1.60 port 80 (http://192.168.1.60:80/) ...
``
## Requirements
Install the required Python packages:

```bash
pip install -r requirements.txt

```bash
chmod +x install.sh

```bash
./install.sh

## Uninstall
./uninstall.sh
