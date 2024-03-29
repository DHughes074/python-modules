# Convert classes to json easily
import json

def toJSON(self, pretty = False):
        return json.dumps(self, default=convert_to_dict, sort_keys=True, indent=4 if pretty else None )

@classmethod
def fromJSON(cls, s):
    return json.loads(s, object_hook=convert_from_dict)

def convert_to_dict(obj):
    """
    A function takes in a custom object and returns a dictionary representation of the object.
    This dict representation includes meta data such as the object's module and class names.
    """
    #https://medium.com/python-pandemonium/json-the-python-way-91aac95d4041

    #  Populate the dictionary with object meta data 
    obj_dict = {
    "__class__": obj.__class__.__name__,
    "__module__": obj.__module__
    }

    #  Populate the dictionary with object properties
    obj_dict.update(obj.__dict__)

    return obj_dict

def convert_from_dict(our_dict):
    """
    Function that takes in a dict and returns a custom object associated with the dict.
    This function makes use of the "__module__" and "__class__" metadata in the dictionary
    to know which object type to create.
    """
    #https://medium.com/python-pandemonium/json-the-python-way-91aac95d4041

    if "__class__" in our_dict:
        # Pop ensures we remove metadata from the dict to leave only the instance arguments
        class_name = our_dict.pop("__class__")
        
        # Get the module name from the dict and import it
        module_name = our_dict.pop("__module__")
        
        # We use the built in __import__ function since the module name is not yet known at runtime
        module = __import__(module_name)
        
        # Get the class from the module
        class_ = getattr(module,class_name)
        
        # Use dictionary unpacking to initialize the object
        obj = class_(**our_dict)
    else:
        obj = our_dict
    return obj
