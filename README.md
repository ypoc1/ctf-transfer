
# CTF File Transfer Tool

**Global Transfer Command for CTFs**

![CTF Transfer](ctf-transfer-small.png)

<p align="center">
  <img src="ctf-transfer-small.png" alt="CTF Transfer" width="300">
</p>

This tool helps you transfer files between machines by setting up a simple Python HTTP server and generating download commands (certutil, iwr, wget, curl). It's designed to streamline file transfers during CTF (Capture the Flag) competitions, making the process quicker and easier.

## Features
- **Easy HTTP Server Setup:** Starts a local Python HTTP server for sharing files.
- **Multiple Download Options:** Generates commands for downloading files using certutil, iwr, wget, and curl.
- **Automatic Zipping:** Automatically zips directories before transfer.
- **Clipboard Integration:** Copies the certutil download command to the clipboard for easy pasting.

## Usage

For transferring a file or folder, run one of the following commands:

```bash
transfer <filename>
transfer <foldername>
```

### Example
```bash
transfer hosts.txt
```

```plaintext
Available network interfaces:
1: lo
2: eth0
3: eth1
Choose an interface by number: 2

Certutil command: certutil -urlcache -split -f "http://192.168.1.60/hosts.txt" hosts.txt
IWR command: iwr -Uri "http://192.168.1.60/hosts.txt" -OutFile "hosts.txt"
Wget command: wget http://192.168.1.60/hosts.txt
Curl command: curl -O http://192.168.1.60/hosts.txt

Certutil command copied to clipboard!
Starting Python HTTP server on 192.168.1.60:80
Press Ctrl+C to stop the server.
Serving HTTP on 192.168.1.60 port 80 (http://192.168.1.60:80/) ...
```

## Requirements

Make sure to install the required Python packages before using the tool:

```bash
pip install -r requirements.txt
```

Then, give the installation script executable permissions:

```bash
chmod +x install.sh
```

And run the installation script:

```bash
./install.sh
```

## Uninstallation

To remove the tool, simply run the uninstallation script:

```bash
./uninstall.sh
```
