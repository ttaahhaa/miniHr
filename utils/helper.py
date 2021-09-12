import os


def root_dir():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_file(filename):
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)
