import os
from datetime import datetime

class Logger:
    def __init__(self, file: str):
        self.file = file

    def _write(self, level: str, msg: str):
        os.makedirs(os.path.dirname(self.file), exist_ok=True)
        
        with open(self.file, "a") as f:
            f.write(f"{datetime.now()} [{level}] {msg}\n")

    def log_info(self, msg: str):
        self._write("INFO", msg)

    def log_error(self, msg: str):
        self._write("ERROR", msg)