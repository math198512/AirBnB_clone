#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb)'

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ': '

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Ignore empty inputs"""
        pass

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting")

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting")

    def do_create(self, args):
        """"Creates a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
            return
        elif args != "BaseModel":
            print("** class doesn't exist")
            return
        new_instance = BaseModel()
        print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
