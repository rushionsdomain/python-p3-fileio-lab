# file_io.py

def write_file(file_name, content):
    """Writes content to a file."""
    with open(f'{file_name}.txt', 'w') as f:
        f.write(content)

def append_file(file_name, content):
    """Appends content to a file."""
    with open(f'{file_name}.txt', 'a') as f:
        f.write(content)

def read_file(file_name):
    """Reads content from a file."""
    with open(f'{file_name}.txt', 'r') as f:
        return f.read()
