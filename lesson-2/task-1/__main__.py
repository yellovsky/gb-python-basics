items_list = [
    1,
    2.0,
    3 + 4j,
    'some string',
    ['a', 1],
    (3, 4),
    {1, 2, 3, 1, 2},
    dict(key='value', other_key='other value'),
    False,
    bool('some val'),
    bytes(22),
    bytearray(b"some text"),
    None,
]


for item in items_list:
    if type(item) is int:
        print(item, 'is int number')
    elif type(item) is float:
        print(item, 'is float number')
    elif type(item) is complex:
        print(item, 'is complex number')
    elif type(item) is str:
        print(item, 'is string')
    elif type(item) is list:
        print(item, 'is list')
    elif type(item) is set:
        print(item, 'is set')
    elif type(item) is dict:
        print(item, 'is dictionary')
    elif type(item) is bool:
        print(item, 'is boolean')
    elif type(item) is tuple:
        print(item, 'is tuple')
    elif type(item) is bytes:
        print(item, 'is bytes')
    elif type(item) is bytearray:
        print(item, 'is bytearray')
    elif item is None:
        print(item, 'is None')
    else:
        print('Hmm...', item, 'has unknown type')
