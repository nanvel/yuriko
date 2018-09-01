import getpass
import subprocess
import sys
import tempfile

from yuriko import settings
from yuriko.manager import NotesManager


def editor(initial):
    with tempfile.NamedTemporaryFile(suffix='note') as tf:
        with open(tf.name, 'w') as f:
            f.write(initial)
        subprocess.call(['vim', tf.name])
        with open(tf.name, 'r') as f:
            return f.read()


def main():
    _, command, *arguments = sys.argv

    password = getpass.getpass('Password:')

    manager = NotesManager(path=settings.YURIKO_DB_PATH, password=password)

    if command == 'init':
        manager.init()
    elif command == 'search':
        q = arguments[0]
        matches = manager.search(prefix=q)
        for m in matches:
            print("- {}".format(m))
    elif command == 'edit':
        key = arguments[0]
        initial = manager.get(key=key)
        value = editor(initial)
        manager.edit(key=key, value=value)
    elif command == 'get':
        key = arguments[0]
        value = manager.get(key)
        print('*{}*'.format(value))
    elif command == 'del':
        key = arguments[0]
        manager.delete(key=key)
    else:
        print("Invalid command. Commands available: init, search <prefix>, edit <key>, get <key>, del <key>.")