@echo off
title Todo App Launcher

echo ========================================
echo         Todo App Launcher
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
if not exist "enhanced_todo_app.py" (
    echo ERROR: Todo app files not found in current directory
    echo Please navigate to the TodoApp directory and run this script again
    echo.
    pause
    exit /b 1
)

echo Todo App files found.
echo.

REM Ask user which version to run
echo Which version would you like to run?
echo 1. Enhanced Todo App (recommended)
echo 2. Basic Todo App
echo 3. Run tests first
echo.
set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" (
    echo Starting Enhanced Todo App...
    python enhanced_todo_app.py
) else if "%choice%"=="2" (
    echo Starting Basic Todo App...
    python todo_app.py
) else if "%choice%"=="3" (
    echo Running tests...
    python test_app.py
    echo.
    echo Press any key to start the Enhanced Todo App...
    pause >nul
    python enhanced_todo_app.py
) else (
    echo Invalid choice. Starting Enhanced Todo App by default...
    python enhanced_todo_app.py
)

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to start the application
    echo Please check the error messages above
    echo.
    pause
    exit /b 1
)

echo.
echo Todo App has been closed.
echo Thank you for using Todo App!
echo.
pause