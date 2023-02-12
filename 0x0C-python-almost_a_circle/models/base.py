#!/usr/bin/python3
"""Defines a class Base."""
import json


class Base:
    """Represent a base of all the classes in this project

    Private Class Attribute:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """Initializes the base
        Args:
            id(int) - identity of the base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        list_objs is a list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        list_dictionaries = []
        with open(filename, "w") as filejson:
            if list_objs is None:
                filejson.write("[]")
            else:
                for obj in list_objs:
                    list_dictionaries.append(obj.to_dictionary())
                filejson.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string

        json_string is a string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Rreturns an instance with all attributes already set

        **dictionary: double pointer to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                dummy = cls(1, 1)
            elif cls.__name__ == 'Square':
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as filejson:
                json_string = filejson.read()
                list_dictionaries = cls.from_json_string(json_string)
                list_objs = []
                for dictionary in list_dictionaries:
                    list_objs.append(cls.create(**dictionary))
                return list_objs
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        Format of the CSV:
            Rectangle: <id>,<width>,<height>,<x>,<y>
            Square: <id>,<size>,<x>,<y>
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or len(list_objs) == 0:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                else:
                    fieldnames = ["id", "width", "height", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize a list of objects from a CSV file"""
        filename = cls.__name__ + ".csv"
        objs = []
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name == 'Square':
                    fieldnames = ["id", "size", "x", "y"]
                else:
                    fieldnames = ["id", "width", "height", "x", "y"]
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                for row in reader:
                    obj = cls.(*row)
                    objs.append(obj)
                return objs
        except:
            return []

