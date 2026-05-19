from pathlib import Path
from datetime import datetime


from utils.execution_context import get_execution_timestamp

class ReportingUtils:
    
    @staticmethod
    def generate_execution_summary(suite_name):
        execution_path = Path(f"test_runs/{get_execution_timestamp()}")
        summary_file = (execution_path/ "execution_summary.txt")
        report_path = (execution_path/"reports")
        logs_path = (execution_path/"logs")
        screenshots_path = (execution_path/"screenshots")

        summary_content = f"""
Suite: {suite_name}
Execution Timestamp:
{get_execution_timestamp()}

Generated Time:
{datetime.now()}

Artifacts:
- Reports: {report_path}
- Logs: {logs_path}
- Screenshots: {screenshots_path}
"""
        execution_path.mkdir(parents=True, exist_ok=True)
        summary_file.write_text(summary_content.strip(), encoding= "utf-8")

        print("\n Execution summary generated. \n")
    
    @staticmethod
    def update_execution_history(suite_name):
        history_file = Path("test_runs/execution_history.txt")
        history_entry = f"""
[{datetime.now()}]
Suite: {suite_name}
Execution Timestamp: {get_execution_timestamp()}
--------------------------------------------
"""
        with open (history_file , 'a', encoding = "utf-8") as file:
            file.write(history_entry)