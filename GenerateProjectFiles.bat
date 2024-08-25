@echo off

REM Check if Python is installed
py --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed on your system.
    echo Please install Python from the following link:
    echo https://www.python.org/downloads/
    start https://www.python.org/downloads/
    pause
)

REM Run the Python setup script
python Scripts\setup.py

pause
