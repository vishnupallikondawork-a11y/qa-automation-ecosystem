@echo off

cd /d %~dp0..

call venv\Scripts\activate

python -m pytest -m smoke ^
--html=test_runs/smoke_report.html ^
--self-contained-html

pause