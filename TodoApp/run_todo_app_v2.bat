@echo off
title Todo App V2 - Sticky Notes Launcher

echo ========================================
echo   Todo App V2 - Sticky Notes Design
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    echo.
    pause
    exit /b 1
)

echo Python is installed.
echo.

REM Check if we're in the right directory
if not exist "todo_app_v2.py" (
    echo ERROR: Todo app files not found in current directory
    echo Please navigate to the TodoApp directory and run this script again
    echo.
    pause
    exit /b 1
)

echo Starting Todo App V2 - Sticky Notes Design...
echo.

python todo_app_v2.py

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to start the application
    echo Please check the error messages above
    echo.
    pause
    exit /b 1
)

echo.
echo Todo App V2 has been closed.
echo Thank you for using Todo App!
echo.
pause
