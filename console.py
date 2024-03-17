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
        args_new = args.split()

        if not args:
            print("** class name missing **")
            return
        elif args_new[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """ Prints the string representation of an instance """
        args_new = args.split(' ')
        if not args_new[0]:
            print("** class name missing **")
        elif args_new[0] != "BaseModel":
            print("** class doesn't exist **")
        elif not args_new[1]:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = '{}.{}'.format(args_new[0], args_new[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        args_new = args.split(' ')
        if not args_new[0]:
            print("** class name missing **")
        elif args_new[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args_new) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = '{}.{}'.format(args_new[0], args_new[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
