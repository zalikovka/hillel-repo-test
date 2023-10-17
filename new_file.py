class File:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
