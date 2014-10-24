def test_version():
    import re
    from twspy import __version__
    assert re.match('[0-9]+\.[0-9]+\.[0-9]+', __version__)


def test_find_packages_exclude():
    import os
    from setuptools import find_packages
    path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    packages = find_packages(path, exclude=['twspy.ib.cfg'])
    for package in packages:
        assert 'cfg' not in package
