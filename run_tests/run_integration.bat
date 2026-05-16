@echo off

cd /d %~dp0..

call venv\Scripts\activate

python -m pytest -m integration ^
--self-contained-html

pause