# hbnb - The ALX AirBnB
![hbnb logo](hbnb.png)

## The Console
This is the creation of a CLI interface and Python model engines for file abstraction and use of classes to store the data and backend operations of the website.


### Command Line Interpreter
#### Starting It
To start it call run the console.py file using `./console.py`.
Once it starts a prompt like this will appear:

```bash
(hbnb)
```

#### Using It
To use it you need to understand the commands present. Here is a list of them:

```bash
Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all     destroy  quit  update
BaseModel  EOF   Review  User   create  help     show
```

As you'll notice it indicates that the commands are documented. For example, here is the documentation for show, User and help. Let us start with show:

```bash
(hbnb) help show
Showing the instance of a class of an id
```

Let's move on to help:

```bash
(hbnb) help help
List available commands with "help" or detailed help with "help cmd".
```

Moving on to User:

```bash
(hbnb) help User
Call functions all, show, update, destroy and count on User
```

As you'll notice you can call functions on User. This is because User is a class in the model hence is a little special. But first let us grasp the fundamentals of the all, show, update, destroy and create functions. Afterwards we will expound on why classes functions are special. Let us focus on each separately.

##### all
all displays all the instances in a particular class or all classes' instances- that is every instance is shown.

```bash
(hbnb) all
[BaseModel] (c97dae67-ea89-4c55-9cba-563a9af2deb4) {'id': 'c97dae67-ea89-4c55-9cba-563a9af2deb4', 'created_at': datetime.datetime(2023, 12, 8, 7, 40, 54, 319757), 'updated_at': datetime.datetime(2023, 12, 8, 7, 40, 54, 319777)}
[User] (3e51b230-cdf3-4fc2-ab7d-552589438f5b) {'id': '3e51b230-cdf3-4fc2-ab7d-552589438f5b', 'created_at': datetime.datetime(2023, 12, 8, 7, 40, 58, 226284), 'updated_at': datetime.datetime(2023, 12, 8, 7, 40, 58, 226298)}
[Place] (ac5efe23-07f4-408d-bae3-dedecafaf9e9) {'id': 'ac5efe23-07f4-408d-bae3-dedecafaf9e9', 'created_at': datetime.datetime(2023, 12, 8, 7, 41, 2, 99985), 'updated_at': datetime.datetime(2023, 12, 8, 7, 41, 2, 99999)}
[State] (1ed6a2c5-b3fe-46ff-ba81-1741af342afc) {'id': '1ed6a2c5-b3fe-46ff-ba81-1741af342afc', 'created_at': datetime.datetime(2023, 12, 8, 7, 41, 9, 967727), 'updated_at': datetime.datetime(2023, 12, 8, 7, 41, 9, 967745)}
```

##### show
show displays an instance of a class with a particular ID

```bash
(hbnb) show User 3e51b230-cdf3-4fc2-ab7d-552589438f5b
[User] (3e51b230-cdf3-4fc2-ab7d-552589438f5b) {'id': '3e51b230-cdf3-4fc2-ab7d-552589438f5b', 'created_at': datetime.datetime(2023, 12, 8, 7, 40, 58, 226284), 'updated_at': datetime.datetime(2023, 12, 8, 7, 40, 58, 226298)}
```

##### update
update adds or modifies a value to an instance of a class based on ID.

```bash
(hbnb) update User 3580352a-f915-4bee-9015-680fdea1d925 first_name "Misati"
(hbnb) show User 3580352a-f915-4bee-9015-680fdea1d925
[User] (3580352a-f915-4bee-9015-680fdea1d925) {'id': '3580352a-f915-4bee-9015-680fdea1d925', 'created_at': datetime.datetime(2023, 12, 8, 7, 46, 44, 687676), 'updated_at': datetime.datetime(2023, 12, 8, 7, 48, 11, 899560), 'first_name': '"Misati"'}
```

##### destroy
destroy deletes an instance of a class

```bash
(hbnb) show User 3580352a-f915-4bee-9015-680fdea1d925
[User] (3580352a-f915-4bee-9015-680fdea1d925) {'id': '3580352a-f915-4bee-9015-680fdea1d925', 'created_at': datetime.datetime(2023, 12, 8, 7, 46, 44, 687676), 'updated_at': datetime.datetime(2023, 12, 8, 7, 48, 11, 899560), 'first_name': '"Misati"'}
(hbnb) destroy User 3580352a-f915-4bee-9015-680fdea1d925
(hbnb) show User 3580352a-f915-4bee-9015-680fdea1d925
** no instance found **
```

##### create
create makes an instance of a class

```bash
(hbnb) create Review
989802b2-d2bf-4fa0-9ea1-b4058e99906c
(hbnb) show Review 989802b2-d2bf-4fa0-9ea1-b4058e99906c
[Review] (989802b2-d2bf-4fa0-9ea1-b4058e99906c) {'id': '989802b2-d2bf-4fa0-9ea1-b4058e99906c', 'created_at': datetime.datetime(2023, 12, 8, 7, 50, 10, 600146), 'updated_at': datetime.datetime(2023, 12, 8, 7, 50, 10, 600161)}
```

##### User (and other classes)
The classes are made to call other functions in order to function calling from the user. This is implemented for example liek this:

```python
def do_User(self, arg):
        """Call functions all, show, update, destroy and count on User"""
        if arg == ".all()":
            self.do_all("User")
```

This enables the user to pass commands like `User.show(<id>)` to show the instance of class instance with the particular ID or `User.count()` to display the number of instances of class User. This works for all other classes also. 

#### Examples
Here is an example a workflow of creating a User class which has the attributes `first_name`, `last_name`, `email` and `password`. We will add the attributes and manipulate the class using the fancy function calling of `<class name>.<function>`.

```bash
(hbnb) create User
6d7e5120-28d3-48c9-98ad-d457943ac92f
(hbnb) User.show("6d7e5120-28d3-48c9-98ad-d457943ac92f")
[User] (6d7e5120-28d3-48c9-98ad-d457943ac92f) {'id': '6d7e5120-28d3-48c9-98ad-d457943ac92f', 'created_at': datetime.datetime(2023, 12, 8, 7, 58, 3, 133195), 'updated_at': datetime.datetime(2023, 12, 8, 7, 58, 3, 133210)}
(hbnb) User.update("6d7e5120-28d3-48c9-98ad-d457943ac92f", "first_name", "Misati")
(hbnb) User.show("6d7e5120-28d3-48c9-98ad-d457943ac92f")
[User] (6d7e5120-28d3-48c9-98ad-d457943ac92f) {'id': '6d7e5120-28d3-48c9-98ad-d457943ac92f', 'created_at': datetime.datetime(2023, 12, 8, 7, 58, 3, 133195), 'updated_at': datetime.datetime(2023, 12, 8, 7, 59, 23, 410683), 'first_name': 'Misati'}
(hbnb) User.update("6d7e5120-28d3-48c9-98ad-d457943ac92f", "last_name", "Nyambane")
(hbnb) User.update("6d7e5120-28d3-48c9-98ad-d457943ac92f", "email", "themisti@alx.app")
(hbnb) User.update("6d7e5120-28d3-48c9-98ad-d457943ac92f", "password", "YouWishYouKnew")
(hbnb) User.show("6d7e5120-28d3-48c9-98ad-d457943ac92f")
[User] (6d7e5120-28d3-48c9-98ad-d457943ac92f) {'id': '6d7e5120-28d3-48c9-98ad-d457943ac92f', 'created_at': datetime.datetime(2023, 12, 8, 7, 58, 3, 133195), 'updated_at': datetime.datetime(2023, 12, 8, 8, 0, 31, 492700), 'first_name': 'Misati', 'last_name': 'Nyambane', 'email': 'themisti@alx.app', 'password': 'YouWishYouKnew'}
(hbnb) User.all()
[User] (6d7e5120-28d3-48c9-98ad-d457943ac92f) {'id': '6d7e5120-28d3-48c9-98ad-d457943ac92f', 'created_at': datetime.datetime(2023, 12, 8, 7, 58, 3, 133195), 'updated_at': datetime.datetime(2023, 12, 8, 8, 0, 31, 492700), 'first_name': 'Misati', 'last_name': 'Nyambane', 'email': 'themisti@alx.app', 'password': 'YouWishYouKnew'}
(hbnb) User.count()
1
(hbnb) User.destroy("6d7e5120-28d3-48c9-98ad-d457943ac92f")
(hbnb) User.show("6d7e5120-28d3-48c9-98ad-d457943ac92f")
** no instance found **
(hbnb) User.all()
(hbnb) User.count()
0
```
