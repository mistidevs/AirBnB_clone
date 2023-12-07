#!/usr/bin/python3
"The console program"
import cmd
import models
from models import storage

class HBNBCommand(cmd.Cmd):
    "HBNB debugging and optimisation console"

    prompt = '(hbnb) '

    def do_create(self, arg):
        "Creating a class"
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
        "Showing the instance of a class of an id"
        classes = ["BaseModel"]
        args = arg.split(" ")
        flag = 0
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
