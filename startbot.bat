@echo off
title Discord Bot Runner
echo ==========================================
echo Starting Discord Bot in Virtual Environment
echo ==========================================

:: Check if venv exists, create if it doesn't
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate virtual environment
call venv\Scripts\activate

:: Install dependencies
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

:: Run the bot (replace index.py with your main file)
echo Running bot...
python bot.py

:: Pause when finished or if it crashes
pause
