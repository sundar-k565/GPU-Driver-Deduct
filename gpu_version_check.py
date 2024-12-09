import subprocess
import os

def check_command(command, args):
    """Run a shell command and return its output or error."""
    try:
        result = subprocess.run(
            [command] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        if result.returncode == 0:
            print(f"Command '{command} {' '.join(args)}' executed successfully:\n{result.stdout}")
        else:
            print(f"Command '{command} {' '.join(args)}' failed:\n{result.stderr}")
    except FileNotFoundError:
        print(f"Command '{command}' not found. Please ensure it is installed.")
    except Exception as e:
        print(f"Error running command '{command}': {e}")

def check_service_status(service_name):
    """Check the status of a systemd service."""
    try:
        result = subprocess.run(
            ["systemctl", "status", service_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if "active (running)" in result.stdout:
            print(f"The service '{service_name}' is active and running.")
        elif "loaded" in result.stdout:
            print(f"The service '{service_name}' is installed but not running.")
        else:
            print(f"The service '{service_name}' is not installed or inactive.")
    except FileNotFoundError:
        print(f"Systemctl not found. Cannot check the status of '{service_name}'.")
    except Exception as e:
        print(f"Error checking service status for '{service_name}': {e}")

if __name__ == "__main__":
    print("Checking 'nvcc -V'...\n")
    check_command("nvcc", ["-V"])
    
    print("\nChecking 'nvidia-smi'...\n")
    check_command("nvidia-smi", [])
    
    print("\nChecking NVIDIA Fabric Manager service...\n")
    check_service_status("nvidia-fabricmanager")

