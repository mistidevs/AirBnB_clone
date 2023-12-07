#!/usr/bin/python3
"The console program"
import cmd


class HBNBCommand(cmd.Cmd):
    "HBNB debugging and optimisation console"

    prompt = '(hbnb)'

    def do_EOF(self, line):
        "Exit when EOF command is given with ^D"
        return True

    def emptyline(self):
        "Do nothing when the user passes an empty line"
        pass

    def do_quit(self, line):
        "Exit when quit command is given"
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
