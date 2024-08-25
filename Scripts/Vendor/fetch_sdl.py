import os
import urllib.request
import zipfile
import re
import shutil

# Constants
SDL_BASE_URL = "https://www.libsdl.org/release/"
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
TEMP_DIR = os.path.join(PROJECT_ROOT, "temp")
SDL_THIRD_PARTY_DIR = os.path.join(PROJECT_ROOT, "Engine", "ThirdParty")
SDL_DONE_FILE = os.path.join(PROJECT_ROOT, "fetch_sdl.done")

def get_latest_sdl_version():
    """Fetch the latest SDL version number from the SDL website."""
    index_url = SDL_BASE_URL
    with urllib.request.urlopen(index_url) as response:
        html = response.read().decode('utf-8')
        match = re.search(r'SDL2-devel-(\d+\.\d+\.\d+)-VC\.zip', html)
        if match:
            return match.group(1)
        else:
            raise RuntimeError("Could not determine the latest SDL version.")

def download_file(url, output_path):
    """Download a file from a URL to a specified output path."""
    print(f"Downloading {url}...")
    urllib.request.urlretrieve(url, output_path)
    print(f"Downloaded to {output_path}")

def extract_zip(zip_path, extract_to):
    """Extract a ZIP file to a specified directory."""
    print(f"Extracting {zip_path}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted to {extract_to}")

def setup_sdl():
    """Download and extract the latest SDL to the ThirdParty directory."""
    try:
        latest_sdl_version = get_latest_sdl_version()
        sdl_filename = f"SDL2-devel-{latest_sdl_version}-VC.zip"
    except Exception as e:
        print(f"Error determining the latest SDL version: {e}")
        sys.exit(1)

    sdl_file_url = SDL_BASE_URL + sdl_filename

    # Ensure the temp directory exists
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

    sdl_output_path = os.path.join(TEMP_DIR, sdl_filename)

    # Download SDL
    download_file(sdl_file_url, sdl_output_path)

    # Ensure the ThirdParty directory exists
    if not os.path.exists(SDL_THIRD_PARTY_DIR):
        os.makedirs(SDL_THIRD_PARTY_DIR)

    # Extract the SDL contents directly into the ThirdParty directory
    extract_zip(sdl_output_path, SDL_THIRD_PARTY_DIR)

    print(f"SDL setup completed. Files are in: {SDL_THIRD_PARTY_DIR}")

if __name__ == "__main__":
    setup_sdl()
