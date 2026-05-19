import os
def get_execution_timestamp():
    return os.environ.get(
        "EXECUTION_TIMESTAMP"
    )