#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb)'
    classes = ["BaseModel", "User"]
    
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
        elif args_new[0] not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(f"{args_new[0]}()")
        storage.save()
        print(new_instance.id)

    def do_show(self, args):
        """ Prints the string representation of an instance """
        args_new = args.split(' ')
        if not args_new[0]:
            print("** class name missing **")
        elif args_new[0] != "BaseModel" and args_new[0] != "User":
            print("** class doesn't exist **")
        elif len(args_new) < 2:
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
        elif args_new[0] != "BaseModel" and args_new[0] != "User":
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

    def do_all(self, args):
        """ Prints all string representation of all instances based
        or not on the class name """
        args_new = args.split(' ')
        if not args_new[0] or args_new[0] == "BaseModel" or args_new[0] == "User":
            objects = storage.all()

            # key = '{}.{}'.format(args_new[0], args_new[1])
            if not args_new[0]:
                new_list = [str(obj) for key, obj in storage.all().items()]
                print(new_list)
            elif args_new[0] == "BaseModel" or args_new[0] == "User":
                obj_list = [str(obj) for key, obj in storage.all().items()
                                        if type(obj).__name__ == args_new[0]]
                print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """ Updates an instance based on the class name and id by
        adding or updating attribute """
        args_new = args.split(' ')
        if not args_new[0]:
            print("** class name missing **")
        elif args_new[0] not in classes:
            print("** class doesn't exist **")
        elif len(args_new) == 1 and args_new[0] in classes:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = '{}.{}'.format(args_new[0], args_new[1])
            if key not in objects:
                print("** no instance found **")
            elif len(args_new) < 3:
                print("** attribute name missing **")
            elif len(args_new) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = args_new[2]
                attr_value = args_new[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass

                setattr(obj, attr_name, attr_value)

                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
