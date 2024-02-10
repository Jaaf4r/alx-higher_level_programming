import json
print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))
#['foo', {'bar': ['baz', None, 1.0, 2]}]
print(json.loads('"\\"foo\\bar"'))
#'"foo\x08ar'
from io import StringIO
io = StringIO('["streaming API"]')
print(json.load(io))
#['streaming API']
