modulePrologueHandlers = [
    'from ._lang.python import cmp',
    'from ._lang.java import Double, Integer',
]

moduleOutputSubs = [
    (r'cls\.NormalizeString\(lhs\)\.compareTo\(cls\.NormalizeString\(rhs\)\)',
     r'cmp(str(lhs), str(rhs))'),

    (r'cls\.NormalizeString\(lhs\)\.compareToIgnoreCase\(cls\.NormalizeString\(rhs\)\)',
     r'cmp(str(lhs).lower(), str(rhs).lower())'),

    (r'else "" \+ value',
     r'else str(value)'),
]
