import json
print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
#'["foo", {"bar": ["baz", null, 1.0, 2]}]'
print("--------------------------------------------------")
print(json.dumps("\"foo\bar"))
#"\"foo\bar"
print("--------------------------------------------------")
print(json.dumps('\u1234'))
#"\u1234"
print("--------------------------------------------------")
print(json.dumps('\\'))
#"\\"
print("--------------------------------------------------")
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
#{"a": 0, "b": 0, "c": 0}
print("--------------------------------------------------")
from io import StringIO
io = StringIO()
json.dump(['streaming API'], io)
print(io.getvalue())
#'["streaming API"]'
