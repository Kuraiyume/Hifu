#!/usr/bin/env python3
import os
import shutil
import sys
import subprocess
import pkg_resources

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip3", "install", package])
        print(f"[+] Successfully installed '{package}'")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error installing '{package}': {e}")
        sys.exit(1)

if os.geteuid() != 0:
    print("[-] Error: This script must be run as root (use sudo).")
    sys.exit(1)

SCRIPT_PATH = "hifu.py"
DEST_DIR = "/usr/local/bin"
DEST_SCRIPT = os.path.join(DEST_DIR, "hifu")

required_packages = ['termcolor', 'rstr']

for package in required_packages:
    try:
        pkg_resources.require(package)
        print(f"[+] '{package}' is already installed.")
    except pkg_resources.DistributionNotFound:
        print(f"[-] '{package}' not found. Installing...")
        install_package(package)

if not os.path.isfile(SCRIPT_PATH):
    print(f"[-] Error: The script '{SCRIPT_PATH}' was not found.")
    sys.exit(1)

try:
    print(f"[+] Copying '{SCRIPT_PATH}' to '{DEST_DIR}'")
    shutil.copy(SCRIPT_PATH, DEST_SCRIPT)

    print(f"[+] Setting execute permissions for '{DEST_SCRIPT}'")
    os.chmod(DEST_SCRIPT, 0o755)

    if os.access(DEST_SCRIPT, os.X_OK):
        print(f"[+] Installation complete. You can now use 'hifu' as a command.")
    else:
        print("[-] Error: The script could not be made executable.")
        sys.exit(1)

except Exception as e:
    print(f"[-] Error: {e}")
    sys.exit(1)
