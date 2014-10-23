modulePrologueHandlers = [
    'from ._lang.python import overloaded',
    'from ._lang.java import Double, Integer, StringBuilder',
    'from .IApiEnum import IApiEnum',
]

moduleOutputSubs = [
    (r'(?m)^(\s+)SEP = 0$', r'\1SEP = chr(0)'),
    (r'\.getBytes\(\)', '.encode()'),
]
