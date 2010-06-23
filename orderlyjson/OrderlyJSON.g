grammar OrderlyJSON;

options {
  language = Python;
}

@header {
import sys
import traceback
from orderly_json import Prefix, Entry, Suffix

from OrderlyJSONLexer import OrderlyJSONLexer
}

@main {
def main(argv, otherArg=None):
  char_stream = ANTLRFileStream(sys.argv[1])
  lexer = OrderlyJSONLexer(char_stream)

  tokens = CommonTokenStream(lexer)
  parser = OrderlyJSONParser(tokens);

  try:
        print parser.orderly_schema()
  except RecognitionException:
	traceback.print_stack()
}

WS : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+   { $channel = HIDDEN; } ;

COMMENT : ('//' | '#') (~'\n')* {$channel = HIDDEN; };

orderly_schema returns [result] : e=unnamed_entries? ';'? {result = e};

named_entries returns [result]
@init {
  result = []
}:
  e=named_entry (
    ';' e2=named_entry { result.append(e2) }
  )* { result = [e] + result };

unnamed_entries returns [result]
@init {
  result = [];
}:
  e=unnamed_entry (
     ';' e2=unnamed_entry { result.append(e2); }
  )* { result = [e] + result };

named_entry returns [result]
  :  (pref=definition_prefix name=property_name suff=definition_suffix) { result = Entry(pref, name, suff); }
  |  (pref=string_prefix name=property_name suff=string_suffix)         { result = Entry(pref, name, suff); }
  ;

unnamed_entry returns [result]
  :  pref=definition_prefix suff=definition_suffix  { result = Entry(pref, None, suff) }
  |  pref=string_prefix suff=string_suffix          { result = Entry(pref, None, suff) }
  ;

definition_prefix returns [result]
  :  'integer' rng=optional_range?                                                            { result = Prefix('integer', rng=('rng' in locals() and rng)) }
  |  'number' rng=optional_range?                                                             { result = Prefix('number', rng=('rng' in locals() and rng))  }
  |  'boolean'                                                                                { result = Prefix('boolean')}
  |  'null'                                                                                   { result = Prefix('null')}
  |  'any'                                                                                    { result = Prefix('any')}
  |  'array' (
      ('{' e=unnamed_entries? ';'? '}' o=OPTIONAL_ADDITIONAL_MARKER? rng=optional_range?)     { result = Prefix('array', entries=('e' in locals() and e), more=('o' in locals() and $o), rng=('rng' in locals() and rng))}
    | ('[' e=unnamed_entry? ';'? ']' rng=optional_range?))                                         { result = Prefix('array', entries=('e' in locals() and e), rng=('rng' in locals() and rng))}
  |  'object' '{' e=named_entries? ';'? '}' o=OPTIONAL_ADDITIONAL_MARKER?                     { result = Prefix('object', entries=('e' in locals() and e), more=('o' in locals() and $o))}
  |  'union'  '{' e=unnamed_entries? ';'? '}'                                                 { result = Prefix('union', entries=('e' in locals() and e))}
  ;

string_prefix returns [result] :  'string' rng=optional_range? {result = Prefix('string', rng=('rng' in locals() and rng))};

string_suffix returns [result] :  regex=OPTIONAL_PERL_REGEX? suff=definition_suffix { suff.regex = regex and $regex.text; result = suff };

definition_suffix returns [result]:
 enums=optional_enum_values?
 d=optional_default_value?
 requires=optional_requires?
 optional=OPTIONAL_OPTIONAL_MARKER?
 extra=optional_extra_properties? {
    result = Suffix(
        enums=('enums' in locals() and enums),
        default_val=('d' in locals() and d),
        requires=('requires' in locals() and requires),
        optional=(('optional' in locals()) and optional),
        extra=('extra' in locals() and extra))
  };

csv_property_names returns [result]
@init {
  result = [];
} :
    prop=property_name (
      ',' prop2=property_name           { result.append(prop2) }
    ) * { result = [prop] + result };

optional_extra_properties returns [result]  :  ('`' obj=json_object '`') {result=obj};

optional_requires returns [result]  :  ('<' p=csv_property_names '>') {result=p};

OPTIONAL_OPTIONAL_MARKER : '?' ;

OPTIONAL_ADDITIONAL_MARKER : '*' ;

optional_enum_values returns [result] : arr=json_array {result = arr};

optional_default_value returns [result] : ('=' d=json_value) {result=d};

optional_range returns [out] : '{' s=json_number? ',' e=json_number? '}' {out = (s, e)};

property_name returns [result]
  : s=json_string                             {result = s}
  | r=PROPERTY_NAME_TOKEN                     {result = $r.text}
  ;

PROPERTY_NAME_TOKEN : ('a' .. 'z' | 'A' .. 'Z' | '_' | '-' )+;

OPTIONAL_PERL_REGEX : ('/' ( (~'/') | '\\/' )+ '/');

///////////// JSON  //////////////////////////

json_object returns [result] :  '{' m=members? '}' {result = m or {}};

members  returns [d]
@init {
  d = dict()
}
:  p1=pair (
  ',' p2=pair { d[p2[0]] = p2[1] }
  ) * {if not p1[0] in d: d[p1[0]] = p1[1]};

pair  returns [out]:  k=json_string ':' v=json_value {out=(k,v)};

json_array returns [result] : '[' elem=elements? ']' {result = elem};

json_number returns [result]
  :  i=INTEGER f=FRAC? e=EXP? {
  exp = 'e' in locals() and e and $e.text or ""
  result = 'f' in locals() and f and float($i.text + $f.text + exp) or int($i.text + exp)
};

elements returns [array]
@init {
  array = []
} : v=json_value (
  ',' v2=json_value { array.append(v2) }
)* {array = [v] + array;};

json_value returns [result]
  :  val=json_string                          {result = val}
  |  val=json_number                          {result = val}
  |  val=json_object                          {result = val}
  |  val=json_array                           {result = val}
  |  'true'                                   {result = True}
  |  'false'                                  {result = False}
  |  'null'                                   {result = None}
  ;

// ----------------------------------------

json_string returns [result] : c=STRING {result = str($c.text[1:-1])};

fragment
QUOTE_OR_BACKSLASH_OR_CONTROL_CHARACTER
  :  '"'
  |  '\\'
  |  '\\' .
  ;

STRING  :  '"' ~'"'* '"';

fragment
HEX  :  'a'..'f'
  |  'A'..'F'
  |  '0'..'9';

ESC : '\\\\' ;

INTEGER   : '-'? ('0'..'9')+ ;

EXP  : ('e' | 'E') ('-' | '+') ?  ('0' .. '9')+ ;

FRAC : '.' ('0' .. '9')+ ;
