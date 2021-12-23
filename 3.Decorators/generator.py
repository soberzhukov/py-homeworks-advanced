import hashlib


def read_file(path_file):
    with open(path_file, 'rb') as f:
        for line in f:
            result_line = hashlib.md5(line).hexdigest()
            yield result_line
