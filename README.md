# python-modules
A collection of useful modules I have created for use in python


## JSONify

A module for easily serializing and deserializing user defined objects in JSON format


### Usage

simply import the module, alias the methods `toJSON(self)` and `fromJSON(s: str)` and implement the following constructor
```
class Example():
    _statuses = {
        '10':'Active',
        '5':'Pre-Active',
        '11':'Inactive',
        '12':'FraudBlock',
        '15':'Pre-Active LoadBlock',
        '16':'LoadBlock',
        '99':'Closed'
    }

    def __init__(self, **entries):
        self.__dict__.update(entries)
        # if nothing is passed in, create default object
        if not len(entries):
            self.currentStatus, self.statusDescription = 5, self._statuses['5']
            self.id = r.randint(1000000,2000000)

    serialize = jsonify.toJSON
    deserialize = jsonify.fromJSON

    def __str__(self):
        return repr(self.__dict__)
```
To serialize an object, simply call the aliased toJSON method on an instance of the class:
```
x = Example()
#note, you can pass pretty=True to return the string formatted for display with newlines, the default behavior outputs a single line of text
x.serialize()
#output: '{"__class__": "Example", "__module__": "__main__", "currentStatus": 5, "id": 1346871, "statusDescription": "Pre-Active"}'
x.serialize(True)
#output: '{\n    "__class__": "Example",\n    "__module__": "__main__",\n    "currentStatus": 5,\n    "id": 1374606,\n    "statusDescription": "Pre-Active"\n}'
#formatted:"""
{
    "__class__": "Example",
    "__module__": "__main__",
    "currentStatus": 5,
    "id": 1698587,
    "statusDescription": "Pre-Active"
}
"""
```
To de-serialize an object, simply call the aliased fromJSON class method and pass it the minified JSON string:
```
tmp = Example.deserialize('{"__class__": "Example", "__module__": "__main__", "currentStatus": 5, "id": 1346871, "statusDescription": "Pre-Active"}')
print(tmp)
#output: {'currentStatus': 5, 'id': 1346871, 'statusDescription': 'Pre-Active'}
#note that the '__class__' and '__module__' fields are not added to the objects instance attributes, they are only used to load the correct class/module and then discarded
```
