import os
import tempfile

class File:
    def __init__(self, file):
        self.file = file
        if not os.path.exists(file):
            with open(file, 'w') as f:
                pass
    
    def __iter__(self):
        file_text = self._list_file()
        return iter(file_text)
                
    def __add__(self, obj):
        file_obj = File(os.path.join(tempfile.gettempdir(), 'new_file'))
        file_obj.write('\n'.join(self._list_file()+obj._list_file()))
        return file_obj
    
    def __str__(self):
        return self.file
        
    def read(self):
        return open(self.file, 'r').read()
    
    def write(self, text):
        with open(self.file, 'w') as f:
            return f.write(text)
        
    def _list_file(self):
        with open(self.file, 'r') as f:
            return list(str(x) for x in f.read().split('\n') if bool(x))
        
        
if __name__ == "__main__":
    file1 = File('f:/1.txt')
    file2 = File('f:/2.txt')
    file1.write('+1')
    new_file = file1 + file2
    for row in new_file:
        print(row)
        
        
# Total tests: 14. Tests failed: 2, Errors: 0. Total time: 0.131.
# Failed test - test_13.
#  E   OSError: [Errno 9] Bad file descriptor

# During handling of the above exception, another exception occurred:
# E   AssertionError: Тест 13.1. Сложение двух экземпляров класса File выбрасывает исключение OSError.
#     assert False        
        
# Total tests: 14. Tests failed: 2, Errors: 0. Total time: 0.148.
# Failed test - test_13.
#  E   TypeError: unsupported operand type(s) for +: 'int' and 'str'

# During handling of the above exception, another exception occurred:
# E   AssertionError: Тест 13.1. Сложение двух экземпляров класса File выбрасывает исключение TypeError.
#     assert False