@echo off

REM Set the path to your virtual environment's activate script
set VENV_PATH=env\Scripts\activate

REM Activate the virtual environment
call %VENV_PATH%

REM Run your Python script
python markov.py
