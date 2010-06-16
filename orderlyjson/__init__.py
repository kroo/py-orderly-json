import orderly_json
import jsonschema
import json

def parse(orderly_string):
  """parses an orderly-json string, and returns a json-schema object"""
  return orderly_json.parseString(orderly_string)

def validate(json_object, orderly_object):
  """validates the json string with an orderly definition"""
  if type(orderly_object) is str:
    orderly_object = parse(orderly_object)
  jsonschema.validate(json_object, orderly_object)


def test():
  example_orderly = """
  object {
    string name;
    string description?;
    string homepage /^http:/;
    integer {1500,3000} invented;
  }*;
  """

  example_json = """
  {
    "name": "orderly",
    "description": "A schema language for JSON",
    "homepage": "http://orderly-json.org",
    "invented": 2009
  }
  """
  example_json = json.loads(example_json)
  schema = parse(example_orderly)
  try:
    validate(example_json, schema)
  except:
    pass
