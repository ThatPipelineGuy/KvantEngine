import os
import subprocess
import sys
import shutil

# Welcome message
print("==========================================")
print("Welcome to the KvantEngine Setup Script")
print("==========================================\n")

# Define directories
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))  # One directory up for the root directory
third_party_dir = os.path.join(root_dir, "Engine", "ThirdParty")
temp_dir = os.path.join(root_dir, "temp")
premake_script = os.path.join(root_dir, "premake5.lua")
fetch_sdl = os.path.join(root_dir, "Scripts", "Vendor", "fetch_sdl.py")
fetch_premake = os.path.join(root_dir, "Scripts", "Vendor", "fetch_premake.py")
premake_exe = os.path.join(third_party_dir, "premake", "premake5.exe")

# Function to run a command and wait for its completion
def run_command(command, wait=True):
    print(f"Running command: {command}")
    process = subprocess.Popen(command, shell=True, cwd=root_dir)
    if wait:
        process.wait()
    return process.returncode

# Function to check for existing third-party libraries
def check_third_party_libs():
    sdl_dir = os.path.join(third_party_dir, "SDL2-2.0.0")
    premake_exists = os.path.exists(premake_exe)

    sdl_exists = os.path.exists(sdl_dir)

    if sdl_exists:
        print("SDL2 already exists.")
    if premake_exists:
        print("Premake already exists.")

    return sdl_exists, premake_exists

# Function to remove the temp directory
def cleanup_temp_dir():
    if os.path.exists(temp_dir):
        print(f"\nRemoving temporary directory: {temp_dir}")
        shutil.rmtree(temp_dir)

# Ensure the temp directory exists
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# Check for existing third-party libraries
sdl_exists, premake_exists = check_third_party_libs()

# Fetch SDL if not already present
if not sdl_exists:
    print("Fetching SDL...")
    run_command(f"python {fetch_sdl}")

# Fetch Premake if not already present
if not premake_exists:
    print("Running Premake setup...")
    run_command(f"python {fetch_premake}")

# Run Premake to generate the project files
print("Running Premake...")
premake_action = "vs2019"
premake_command = f"{premake_exe} {premake_action} --file={premake_script}"
premake_result = run_command(premake_command)

if premake_result != 0:
    print(f"Premake failed with exit code {premake_result}.")
    print(f"Command: {premake_command}")
    cleanup_temp_dir()
    sys.exit(1)

# Clean up the temporary directory
cleanup_temp_dir()
