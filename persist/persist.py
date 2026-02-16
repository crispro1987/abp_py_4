import json

class PersistJSON:

    def __init__(self, file: str):
        self.file = file

    def save(self, data: list):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        try:
            with open(self.file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []