#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    def do_quit(self, line):
    """Quit command to exit the program"""
        exit()

    def do_EOF(self, line):
    """EOF command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
