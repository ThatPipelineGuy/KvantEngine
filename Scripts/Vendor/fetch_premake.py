import os
import urllib.request
import zipfile
import shutil

# Define directories
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))  # Adjust path as needed
third_party_dir = os.path.join(root_dir, "Engine", "ThirdParty")
premake_dir = os.path.join(third_party_dir, "premake")
premake_exe = os.path.join(premake_dir, "premake5.exe")
temp_dir = os.path.join(root_dir, "temp")

# Function to download files
def download_file(url, output_path):
    print(f"Downloading {url}...")
    urllib.request.urlretrieve(url, output_path)

# Function to extract zip files
def extract_zip(file_path, extract_to):
    print(f"Extracting {file_path}...")
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted to {extract_to}")

# Ensure the temp directory exists
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# Check if Premake is installed
print("Checking for Premake...")
if not os.path.exists(premake_exe):
    premake_url = "https://github.com/premake/premake-core/releases/download/v5.0.0-alpha15/premake-5.0.0-alpha15-windows.zip"
    premake_zip = os.path.join(temp_dir, "premake.zip")
    download_file(premake_url, premake_zip)
    extract_zip(premake_zip, premake_dir)
else:
    print("Premake already exists.")

# Clean up the temporary directory
if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir)

print("Premake setup completed.")
