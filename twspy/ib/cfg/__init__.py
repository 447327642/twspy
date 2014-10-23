from java2python.config import default
from java2python.mod import basic


default.modulePrologueHandlers.remove(basic.shebangLine)

moduleOutputSubs = [
    (r'(\s+)def equals\(', r'\1def __eq__('),
    (r'(\W)self ==', r'\1self is'),
    (r'== None(\W)', r'is None\1'),
    (r'!= None(\W)', r'is not None\1'),
    (r'\.get\((.*?)\)', r'[\1]'),
]
