#!/usr/bin/python3
"""The console program"""
import cmd
import models
from models import storage

class HBNBCommand(cmd.Cmd):
    """HBNB debugging and optimisation console"""

    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creating a class"""
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] == "BaseModel":
            instance = models.base_model.BaseModel()
            instance.save()
            print(instance.id)
            storage.new(instance)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Showing the instance of a class of an id"""
        classes = ["BaseModel"]
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] in classes:
            if len(args) == 2:
                key = args[0] + "." + args[1]
                if key not in storage.objects:
                    print("** no instance found **")
                    return
                instance = str(storage.objects[key])
                print(instance)
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Showing the instance of a class of an id"""
        classes = ["BaseModel"]
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] in classes:
            if len(args) == 2:
                key = args[0] + "." + args[1]
                if key not in storage.objects:
                    print("** no instance found **")
                    return
                del storage.objects[key]
                storage.save()
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Printing either all class instances or all instances of a class"""
        classes = ["BaseModel"]
        args = arg.split(" ")
        if len(arg) == 0:
            for key, value in storage.objects.items():
                print(value)
        elif len(args) == 1:
            if args[0] in classes:
                for key, value in storage.objects.items():
                    parts = key.split(".")
                    if parts[0] == args[0]:
                        print(value)
                        print(key)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updating class attributes """
        args = arg.split(" ")
        classes = ["BaseModel"]
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if len(args) == 2:
            if key not in storage.objects:
                print("** no instance found **")
                return
            else:
                print("** attribute name missing **")
                return
        if len(args) == 3:
            print("** value missing **")
            return

        instance = storage.objects[key]
        attr_name = args[2]
        attr_value = args[3]
        setattr(instance, attr_name, attr_value)
        instance.save()
        
    def do_EOF(self, line):
        "Exit when EOF command is given with ^D"
        print("")
        return True

    def emptyline(self):
        "Do nothing when the user passes an empty line"
        pass

    def do_quit(self, line):
        "Exit when quit command is given"
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
