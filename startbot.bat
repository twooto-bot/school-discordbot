@echo off
title Discord Bot Runner
echo ==========================================
echo Starting Discord Bot in Virtual Environment
echo ==========================================

:: Check if venv exists, create if it doesn't
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv

   :: Use venv's Python to install dependencies
   echo Installing dependencies from requirements.txt...
   venv\Scripts\python.exe -m pip install -r requirements.txt
)

:: Activate virtual environment
call venv\Scripts\activate

:: Run the bot (replace index.py with your main file)
echo Running bot...
python bot.py

:: Pause when finished or if it crashes
pause