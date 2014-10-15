moduleOutputSubs = [
    (r'(?s)(class EClientErrors.+?\n.+?\n)(.+?)\n\n( +def __init__.+)', r'\1\3\n\2'),
]
