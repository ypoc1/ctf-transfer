#!/usr/bin/env python3
import os
import socket
import psutil
import sys
import pyperclip
import shutil
from subprocess import Popen

def get_network_interfaces():
    interfaces = psutil.net_if_addrs()
    return {idx+1: iface for idx, iface in enumerate(interfaces)}

def display_interfaces(interfaces):
    print("Available network interfaces:")
    for idx, iface in interfaces.items():
        print(f"{idx}: {iface}")

def get_ipv4_address(interface_info):
    for addr in interface_info:
        if addr.family == socket.AF_INET:
            return addr.address
    return None

def generate_download_commands(file_name, ip):
    certutil_command = f'certutil -urlcache -split -f "http://{ip}/{os.path.basename(file_name)}" {os.path.basename(file_name)}'
    iwr_command = f'iwr -Uri "http://{ip}/{os.path.basename(file_name)}" -OutFile "{os.path.basename(file_name)}"'
    wget_command = f'wget http://{ip}/{os.path.basename(file_name)}'
    curl_command = f'curl -O http://{ip}/{os.path.basename(file_name)}'
    return certutil_command, iwr_command, wget_command, curl_command

def start_http_server(interface_ip):
    print(f"Starting Python HTTP server on {interface_ip}:80")
    os.chdir('.')
    server_process = Popen([sys.executable, "-m", "http.server", "80", "--bind", interface_ip])
    return server_process

def copy_to_clipboard(text):
    pyperclip.copy(text)
    print("Certutil command copied to clipboard!")

def zip_directory(dir_path):
    zip_file_name = f"{dir_path}.zip"
    shutil.make_archive(dir_path, 'zip', dir_path)
    return zip_file_name

def main():
    # Step 1: Check for filename argument
    if len(sys.argv) != 2:
        print("Usage: transfer <filename_or_directory>")
        return

    path = os.path.abspath(sys.argv[1])

    if os.path.isdir(path):
        print(f"Zipping directory '{path}'...")
        file_name = zip_directory(path)
    elif os.path.isfile(path):
        file_name = path
    else:
        print(f"Error: Path '{path}' does not exist.")
        return

    # Step 2: Show network interfaces
    interfaces = get_network_interfaces()
    display_interfaces(interfaces)

    # Step 3: Ask the user to choose an interface
    try:
        choice = int(input("Choose an interface by number: "))
        if choice not in interfaces:
            raise ValueError("Invalid choice.")
    except ValueError as ve:
        print(f"Error: {ve}")
        return

    interface_info = psutil.net_if_addrs()[interfaces[choice]]
    interface_ip = get_ipv4_address(interface_info)

    if interface_ip is None:
        print(f"Error: Could not find IPv4 address for interface {interfaces[choice]}")
        return

    # Step 4: Generate and display certutil, iwr, wget, and curl commands
    certutil_command, iwr_command, wget_command, curl_command = generate_download_commands(file_name, interface_ip)
    print(f"Certutil command: {certutil_command}")
    print(f"IWR command: {iwr_command}")
    print(f"Wget command: {wget_command}")
    print(f"Curl command: {curl_command}")

    # Step 5: Copy certutil command to clipboard
    copy_to_clipboard(certutil_command)

    # Step 6: Start the HTTP server on the chosen interface
    try:
        server_process = start_http_server(interface_ip)
        print("Press Ctrl+C to stop the server.")
        server_process.wait()
    except KeyboardInterrupt:
        print("\nStopping the HTTP server...")
        server_process.terminate()
        server_process.wait()
        print("HTTP server stopped.")

if __name__ == "__main__":
    main()
