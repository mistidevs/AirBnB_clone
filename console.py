#!/usr/bin/python3
"""The console program"""
import cmd
import models
from models import storage
import copy


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
        elif args[0] == "User":
            instance = models.user.User()
        elif args[0] == "State":
            instance = models.state.State()
        elif args[0] == "City":
            instance = models.city.City()
        elif args[0] == "Amenity":
            instance = models.amenity.Amenity()
        elif args[0] == "Place":
            instance = models.place.Place()
        elif args[0] == "Review":
            instance = models.review.Review()
        else:
            print("** class doesn't exist **")
        instance.save()
        print(instance.id)
        storage.new(instance)

    def do_show(self, arg):
        """Showing the instance of a class of an id"""
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
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
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
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
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
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
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updating class attributes """
        args = arg.split(" ")
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) >= 2:
            if key not in storage.objects:
                print("** no instance found **")
                return
            elif len(args) == 2:
                print("** attribute name missing **")
                return
        if len(args) == 3:
            print("** value missing **")
            return

        key = args[0] + "." + args[1]
        instance_dic = storage.all()
        attr_name = args[2]
        attr_value = args[3]
        list1 = ["id", "created_at", "updated_at"]
        if key i in instance_dic:
            if attr_name not in list1:
                if hasattr(instance_dic[key], attr_name):
                    attr_type = type(getattr(instance_dic[key], attr_name))
                    setattr(instance_dic[key], attr_name, attr_type(attr_value))
                else:
                    setattr(instance_dic[key], attr_name, attr_value)

                instance_dic[key].save()
            else:
                print(f"{attr_name} can't be apdated")
        else:
            print("No instance found")

    def do_User(self, arg):
        """Call functions all, show, update, destroy and count on User"""
        if arg == ".all()":
            self.do_all("User")
        elif arg == ".count()":
            counter = 0
            for key in storage.objects:
                args = key.split(".")
                if args[0] == "User":
                    counter += 1
            print(counter)
        else:
            parts = arg.split("(")
            cmd = parts[0]
            if cmd == ".show":
                args = parts[1].split("\"")
                argi = args[1]
                command = "User " + argi
                self.do_show(command)
            elif cmd == ".destroy":
                args = parts[1].split("\"")
                argi = args[1]
                command = "User " + argi
                self.do_destroy(command)
            elif cmd == ".update":
                args = parts[1].split(", ")
                arg_1 = args[0].split("\"")[1]
                arg_2 = args[1].split("\"")[1]
                arg_3 = args[2].split("\"")[1]
                command = "User " + arg_1 + " " + arg_2 + " " + arg_3
                self.do_update(command)

    def do_BaseModel(self, arg):
        """Call functions all, show, update, destroy and count on BaseModel"""
        if arg == ".all()":
            self.do_all("BaseModel")
        elif arg == ".count()":
            counter = 0
            for key in storage.objects:
                args = key.split(".")
                if args[0] == "BaseModel":
                    counter += 1
            print(counter)
        else:
            parts = arg.split("(")
            cmd = parts[0]
            if cmd == ".show":
                args = parts[1].split("\"")
                argi = args[1]
                command = "BaseModel " + argi
                self.do_show(command)
            elif cmd == ".destroy":
                args = parts[1].split("\"")
                argi = args[1]
                command = "BaseModel " + argi
                self.do_destroy(command)
            elif cmd == ".update":
                args = parts[1].split(", ")
                arg_1 = args[0].split("\"")[1]
                arg_2 = args[1].split("\"")[1]
                arg_3 = args[2].split("\"")[1]
                command = "BaseModel " + arg_1 + " " + arg_2 + " " + arg_3
                self.do_update(command)

    def do_State(self, arg):
        """Call functions all, show, update, destroy and count on State"""
        if arg == ".all()":
            self.do_all("State")
        elif arg == ".count()":
            counter = 0
            for key in storage.objects:
                args = key.split(".")
                if args[0] == "State":
                    counter += 1
            print(counter)
        else:
            parts = arg.split("(")
            cmd = parts[0]
            if cmd == ".show":
                args = parts[1].split("\"")
                argi = args[1]
                command = "State " + argi
                self.do_show(command)
            elif cmd == ".destroy":
                args = parts[1].split("\"")
                argi = args[1]
                command = "State " + argi
                self.do_destroy(command)
            elif cmd == ".update":
                args = parts[1].split(", ")
                arg_1 = args[0].split("\"")[1]
                arg_2 = args[1].split("\"")[1]
                arg_3 = args[2].split("\"")[1]
                command = "State " + arg_1 + " " + arg_2 + " " + arg_3
                self.do_update(command)

    def do_City(self, arg):
        """Call functions all, show, update, destroy and count on City"""
        if arg == ".all()":
            self.do_all("City")
        elif arg == ".count()":
            counter = 0
            for key in storage.objects:
                args = key.split(".")
                if args[0] == "City":
                    counter += 1
            print(counter)
        else:
            parts = arg.split("(")
            cmd = parts[0]
            if cmd == ".show":
                args = parts[1].split("\"")
                argi = args[1]
                command = "City " + argi
                self.do_show(command)
            elif cmd == ".destroy":
                args = parts[1].split("\"")
                argi = args[1]
                command = "City " + argi
                self.do_destroy(command)
            elif cmd == ".update":
                args = parts[1].split(", ")
                arg_1 = args[0].split("\"")[1]
                arg_2 = args[1].split("\"")[1]
                arg_3 = args[2].split("\"")[1]
                command = "City " + arg_1 + " " + arg_2 + " " + arg_3
                self.do_update(command)

    def do_Amenity(self, arg):
        """Call functions all, show, update, destroy and count on Amenity"""
        if arg == ".all()":
            self.do_all("Amenity")
        elif arg == ".count()":
            counter = 0
            for key in storage.objects:
                args = key.split(".")
                if args[0] == "Amenity":
                    counter += 1
            print(counter)
        else:
            parts = arg.split("(")
            cmd = parts[0]
            if cmd == ".show":
                args = parts[1].split("\"")
                argi = args[1]
                command = "Amenity " + argi
                self.do_show(command)
            elif cmd == ".destroy":
                args = parts[1].split("\"")
                argi = args[1]
                command = "Amenity " + argi
                self.do_destroy(command)
            elif cmd == ".update":
                args = parts[1].split(", ")
                arg_1 = args[0].split("\"")[1]
                arg_2 = args[1].split("\"")[1]
                arg_3 = args[2].split("\"")[1]
                command = "Amenity " + arg_1 + " " + arg_2 + " " + arg_3
                self.do_update(command)

    def do_Place(self, arg):
        """Call functions all, show, update, destroy and count on Place"""
        if arg == ".all()":
            self.do_all("Place")
        elif arg == ".count()":
            counter = 0
            for key in storage.objects:
                args = key.split(".")
                if args[0] == "Place":
                    counter += 1
            print(counter)
        else:
            parts = arg.split("(")
            cmd = parts[0]
            if cmd == ".show":
                args = parts[1].split("\"")
                argi = args[1]
                command = "Place " + argi
                self.do_show(command)
            elif cmd == ".destroy":
                args = parts[1].split("\"")
                argi = args[1]
                command = "Place " + argi
                self.do_destroy(command)
            elif cmd == ".update":
                args = parts[1].split(", ")
                arg_1 = args[0].split("\"")[1]
                arg_2 = args[1].split("\"")[1]
                arg_3 = args[2].split("\"")[1]
                command = "Place " + arg_1 + " " + arg_2 + " " + arg_3
                self.do_update(command)

    def do_Review(self, arg):
        """Call functions all, show, update, destroy and count on Review"""
        if arg == ".all()":
            self.do_all("Review")
        elif arg == ".count()":
            counter = 0
            for key in storage.objects:
                args = key.split(".")
                if args[0] == "Review":
                    counter += 1
            print(counter)
        else:
            parts = arg.split("(")
            cmd = parts[0]
            if cmd == ".show":
                args = parts[1].split("\"")
                argi = args[1]
                command = "Review " + argi
                self.do_show(command)
            elif cmd == ".destroy":
                args = parts[1].split("\"")
                argi = args[1]
                command = "Review " + argi
                self.do_destroy(command)
            elif cmd == ".update":
                args = parts[1].split(", ")
                arg_1 = args[0].split("\"")[1]
                arg_2 = args[1].split("\"")[1]
                arg_3 = args[2].split("\"")[1]
                command = "Review " + arg_1 + " " + arg_2 + " " + arg_3
                self.do_update(command)
                
        
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
