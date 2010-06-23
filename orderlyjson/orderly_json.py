import json
import sys
import traceback
import os.path

sys.path.append(os.path.dirname(__file__))

class Prefix(object):
  def __init__(self, kind, entries=None, rng=None, more=None):
    super(Prefix, self).__init__()
    self.kind = kind
    self.entries = entries
    self.rng = rng
    self.more = more

  def __repr__(self):
    return json.dumps(self.get_object(), indent=4)

  def get_object(self):
    output={}
    output['type'] = self.kind
    if self.entries is not None:
      if self.kind == "object":
        output['properties'] = {}
        for entry in self.entries:
          obj =entry.get_object()
          keyname = obj.keys()[0]
          output['properties'][keyname] = obj[keyname]
      elif self.kind == "array":
        if type(self.entries) is not list: self.entries = [self.entries];
        output['items'] = map(lambda x: x.get_object(), self.entries)
    if self.rng is not None:
      if not self.rng[0] is None:
        output['minimum'] = self.rng[0]
      if not self.rng[1] is None:
        output['maximum'] = self.rng[1]
    if self.more:
      output['additionalProperties'] = True
    return output

class Entry(object):
  def __init__(self, prefix, name, suffix):
    super(Entry, self).__init__()
    self.prefix = prefix
    self.name = name
    self.suffix = suffix

  def __repr__(self):
    return json.dumps(self.get_object(), indent=4)

  def get_object(self):
    prefix = self.prefix.get_object()
    suffix = self.suffix.get_object()

    combined = prefix
    for key in suffix:
      combined[key] = suffix[key]


    if self.name is not None:
      output = {
        self.name : combined
      }
    else:
      output = combined

    return output

class Suffix(object):
  def __init__(self, enums=None, default_val=None, requires=None, optional=None, extra=None):
    super(Suffix, self).__init__()
    self.enums = enums
    self.default_val = default_val
    self.requires = requires
    self.optional = optional
    self.extra = extra
    self.regex = None

  def __repr__(self):
    return json.dumps(self.get_object(), indent=4)

  def get_object(self):
    result = {
      'enum' : self.enums,
      'default' : self.default_val,
      'requires' : self.requires,
      'optional' : self.optional and True or None,
      'extra' : self.extra,
      'pattern' : self.regex
    }
    for key in result.keys():
      if result[key] is None:
        del result[key]
    if 'pattern' in result:
      result['pattern'] = result['pattern'][1:-1] # take off the beginning and ending /s
    return result

# orderlyjson parser and lexer requires this file, so we need to move the actual interface down here
def main(argv=sys.argv):
  print parseString(open(sys.argv[1]).read())

def parseString(string):
  if 'ANTLRStringStream' not in globals():
    from OrderlyJSONLexer import ANTLRStringStream
  result = parseStream(ANTLRStringStream(string))
  return result[0].get_object()

def parseFile(path):
  if 'ANTLRFileStream' not in globals():
    from OrderlyJSONLexer import ANTLRFileStream
  return parseStream(ANTLRFileStream(path))[0].get_object()

def parseStream(char_stream):
  try:
    from OrderlyJSONLexer import OrderlyJSONLexer
    from OrderlyJSONParser import ANTLRFileStream, ANTLRStringStream, CommonTokenStream, OrderlyJSONParser, RecognitionException
  except ImportError:
    pass #circular import

  lexer = OrderlyJSONLexer(char_stream)

  tokens = CommonTokenStream(lexer)
  parser = OrderlyJSONParser(tokens);

  try:
    result = parser.orderly_schema()
  except RecognitionException:
    traceback.print_stack()
  return result


if __name__ == "__main__":
  main()
