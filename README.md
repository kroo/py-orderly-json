# orderlyjson Python Library #

## Usage ##

    >>> import orderlyjson, json
    >>> orderlydoc = open('test.orderly').read()
    >>> print orderlydoc
    object {
      string name;
      string description?;
      string homepage /^http:/;
      integer {1500,3000} invented;
    }*;

    >>> print json.dumps(
    ...    orderlyjson.parse(orderlydoc), indent=4)
    {
        "additionalProperties": true,
        "type": "object",
        "properties": {
            "invented": {
                "minimum": 1500,
                "type": "integer",
                "maximum": 3000
            },
            "homepage": {
                "pattern": "^http:",
                "type": "string"
            },
            "name": {
                "type": "string"
            },
            "description": {
                "optional": true,
                "type": "string"
            }
        }
    }

    >>> jsondoc = open('test.json').read()
    >>> print jsondoc
    {
      "name": "orderly",
      "description": "A schema language for JSON",
      "homepage": "http://orderly-json.org",
      "invented": 2009
    }

    >>> orderlyjson.validate(json.loads(jsondoc), orderlydoc)
    >>> badjsondoc = """
    ... {
    ...   "name": "orderly",
    ...   "description": "A schema language for JSON",
    ...   "homepage": "http://orderly-json.org",
    ...   "invented": 4009
    ... }
    ... """
    >>> orderlyjson.validate(json.loads(badjsondoc), orderlydoc)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "orderlyjson/__init__.py", line 13, in validate
        jsonschema.validate(json_object, orderly_object)
      File "orderlyjson/jsonschema/__init__.py", line 101, in validate
        return v.validate(data,schema)
      File "orderlyjson/jsonschema/validator.py", line 410, in validate
        self._validate(data, schema)
      File "orderlyjson/jsonschema/validator.py", line 413, in _validate
        self.__validate("_data", {"_data": data}, schema)
      File "orderlyjson/jsonschema/validator.py", line 439, in __validate
        validator(data, fieldname, schema, new_schema.get(schemaprop))
      File "orderlyjson/jsonschema/validator.py", line 128, in validate_properties
        self.__validate(eachProp, value, properties.get(eachProp))
      File "orderlyjson/jsonschema/validator.py", line 439, in __validate
        validator(data, fieldname, schema, new_schema.get(schemaprop))
      File "orderlyjson/jsonschema/validator.py", line 230, in validate_maximum
        raise ValueError("Value %r for field '%s' is greater than maximum value: %f" % (value, fieldname, maximum))
    ValueError: Value 4009 for field 'invented' is greater than maximum value: 3000.000000

## Validation Tool ##

As a starting point, theres a short python script for validating a json file with
an associated orderly schema in the tools directory named `validate.py`; thanks to
**Jens Hübel** for the contribution:

> Usage is then like this:
>
>     python validate.py invoice.json PropDef.orderly
>
> gives:
>
>     OK
>
> or:
>
>     python validate.py invoice_bad.json PropDef.orderly
>
> results in:
>
>     Validation FAILED
>
>     Value 'XXX' for field 'updatability' is not in the enumeration: ['readonly', 're adwrite', 'whencheckedout', 'oncreate']


## Thanks and License ##

Thanks to **Lloyd Hilaiel** for the documentation and language specification at
[orderly-json.org](http://orderly-json.org/ "Orderly JSON").

This code is licensed under the MIT license. It currently includes the
jsonschema library found [here](http://code.google.com/p/jsonschema/);
