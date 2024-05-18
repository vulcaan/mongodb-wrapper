from mongodbwrapper import MongoDBWrapper
import shlex
from ast import literal_eval
from json import loads


def main():
    print("Welcome to MongoDB Wrapper!")
    mongo = MongoDBWrapper()
    while True:
        print("> ", end="")
        string = input()
        if string == "exit":
            break
        command = shlex.split(string)
        result = ""
        try:
            if command[0] == "connect" and len(command) == 2:
                result = mongo.connect(command[1])
            elif command[0] == "list" and len(command) <= 3:
                result = list(mongo.list(*command[1:]))
            elif command[0] == "list" and len(command) == 4:
                result = list(mongo.list(*command[1:-1], loads(command[-1])))
            elif command[0] == "insert" and len(command) == 4:
                result = mongo.insert(*command[1:-1], loads(command[-1]))
            elif command[0] == "update" and len(command) == 5:
                result = mongo.update(
                    *command[1:-2], loads(command[-2]), loads(command[-1])
                )
            elif command[0] == "remove" and len(command) == 4:
                result = mongo.remove(*command[1:-1], loads(command[-1]))
            else:
                print("Invalid command! Try again...")
        except Exception as e:
            print(f"Error: {repr(e)}")
        print(f"Result: {result}")

    print("Bye!")


if __name__ == "__main__":
    main()
