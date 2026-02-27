import json
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

print(json.dumps("\"foo\bar"))

print(json.dumps('\u1234'))

print(json.dumps('\\'))

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

from io import StringIO
io = StringIO()
json.dump(['streaming API'], io)
io.getvalue()

import json
print(json.dumps({'6': 7, '4': 5}, sort_keys=True, indent=4))

import json
def custom_json(obj):
    if isinstance(obj, complex):
        return {'__complex__': True, 'real': obj.real, 'imag': obj.imag}
    raise TypeError(f'Cannot serialize object of {type(obj)}')

json.dumps(1 + 2j, default=custom_json)

import json
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

json.loads('"\\"foo\\bar"')

from io import StringIO
io = StringIO('["streaming API"]')
json.load(io)

import json
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct

json.loads('{"__complex__": true, "real": 1, "imag": 2}',
    object_hook=as_complex)

import decimal
json.loads('1.1', parse_float=decimal.Decimal)

import json
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        # Let the base class default method raise the TypeError
        return super().default(obj)

json.dumps(2 + 1j, cls=ComplexEncoder)

ComplexEncoder().encode(2 + 1j)

list(ComplexEncoder().iterencode(2 + 1j))

echo '{"json":"obj"}' | python -m json



echo '{1.2:3.4}' | python -m json

