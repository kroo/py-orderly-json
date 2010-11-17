import sys, os.path

sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "..")))

import orderlyjson, json

def main(jsonFile, orderlyFile):
  orderlydoc = open(orderlyFile).read();
  jsondoc = open(jsonFile).read();

  try:
    orderlyjson.validate(json.loads(jsondoc), orderlydoc);
    print "OK";
    return 0;

  except Exception as exc:
    print "Validation FAILED";
    print exc;
    return -1;

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2]);
