#!/usr/bin/env python3
import os
import sys
import shutil
import stat

if os.geteuid() != 0:
    print("[-] Error: This script must be run as root (use sudo).")
    sys.exit(1)

script_path = "hifu.py"
dest_dir = "/usr/local/bin"
dest_script = os.path.join(dest_dir, "hifu")

if not os.path.isfile(script_path):
    print(f"[-] Error: The script '{script_path}' was not found.")
    sys.exit(1)

try:
    print(f"[+] Copying '{script_path}' to '{dest_dir}'")
    shutil.copy(script_path, dest_script)
except Exception as e:
    print(f"[-] Error: Failed to copy the script. {e}")
    sys.exit(1)

try:
    print(f"[+] Setting execute permissions for '{dest_script}'")
    os.chmod(dest_script, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
except Exception as e:
    print(f"[-] Error: Failed to set execute permissions. {e}")
    sys.exit(1)

if os.access(dest_script, os.X_OK):
    print(f"[+] Installation complete. You can now use 'hifu' as a command.")
else:
    print("[-] Error: The script could not be made executable.")
    sys.exit(1)

