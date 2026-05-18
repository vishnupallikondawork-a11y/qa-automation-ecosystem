import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from utils.execution_config import SUITES

def run_suite(suite_name):

    if suite_name not in SUITES:
        print(f"Invalid suite: {suite_name}")
        print(
            f"available suites:"
            f"{list(SUITES.keys())}"
            )
        return
    command = (
        f"python -m pytest -m {SUITES[suite_name]} --self-contained-html"
    )

    print(
        f"\n Executing {suite_name} suite... \n"
    )
    os.system(command)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("please provide suite name")
    else:
        run_suite(sys.argv[1])