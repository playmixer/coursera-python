import os

class FileReader:
    def __init__(self, file):
        self._file = file
        
    def read(self):
        try:
            with open(self._file) as f:
                return f.read()
        except FileNotFoundError:
            return ""
